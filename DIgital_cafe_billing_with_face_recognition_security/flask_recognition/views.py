from flask import Flask,render_template, redirect,url_for,request
import cv2,os
import numpy as np

from sklearn.model_selection import train_test_split


from PIL import Image

from time import time
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pickle
from recognition import recognize
from train_face import train

app=Flask(__name__)

@app.route("/detect")
def detect():
    recognize()
        #cv2.imshow("Face",img)
        #if(cv2.waitKey(1) == ord('q')):
        #    break
        #elif(userId != 0):
        #    cv2.waitKey(1000)
        #    cam.release()
        #    cv2.destroyAllWindows()
        #    return redirect('records/details/'+str(userId))
    return redirect(url_for('index'))


@app.route("/admin")
def admin():
    pass
@app.route("/details")
def details():
    return render_template("details.html")

@app.route("/")
def index():

    return render_template('index.html')
@app.route("/error")
def errorImg():
    return render_template('error.html')

@app.route("/create_dataset",methods=["GET","POST"])
def create_dataset():
    #print request.POST

        if request.method=="POST":
            name=request.form.get("userId")
         
            cam = cv2.VideoCapture(1)
            detector=cv2.CascadeClassifier('Classifiers/face.xml')
            i=0
            offset=50


            #name=input('enter your id')
            while True:
                ret, im =cam.read()
                gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
                faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
                for(x,y,w,h) in faces:
                    i=i+1
                    cv2.imwrite("dataSet/face-"+name +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
                    cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
                    cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
                    cv2.waitKey(100)
                if i>100:
                    cam.release()
                    cv2.destroyAllWindows()
                    break
       


        return redirect(url_for('index'))


@app.route("/trainer")

def trainer():

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        cascadePath = "Classifiers/face.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath);
        path = 'dataSet'

        def get_images_and_labels(path):
             image_paths = [os.path.join(path, f) for f in os.listdir(path)]
             # images will contains face images
             images = []
             # labels will contains the label that is assigned to the image
             labels = []
             for image_path in image_paths:
                 # Read the image and convert to grayscale
                 image_pil = Image.open(image_path).convert('L')
                 # Convert the image format into numpy array
                 image = np.array(image_pil, 'uint8')
                 # Get the label of the image
                 nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
                 #nbr=int(''.join(str(ord(c)) for c in nbr))
                 print (nbr)
                 # Detect the face in the image
                 faces = faceCascade.detectMultiScale(image)
                 # If face is detected, append the face to images and the label to labels
                 for (x, y, w, h) in faces:
                     images.append(image[y: y + h, x: x + w])
                     labels.append(nbr)
                     cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
                     cv2.waitKey(10)
             # return the images list and labels list
             return images, labels


        images, labels = get_images_and_labels(path)
        cv2.imshow('test',images[0])
        cv2.waitKey(1)

        recognizer.train(images, np.array(labels))
        recognizer.write('trainer/trainer.yml')
        #recognizer.save('trainer/trainer.yml')
        cv2.destroyAllWindows()

        return redirect(url_for('index'))







@app.route("/eigenTrain")
def eigenTrain(request):
    path ='ml/dataset'

    # Fetching training and testing dataset along with their image resolution(h,w)
    ids, faces, h, w= df.getImagesWithID(path)
    print ('features'+str(faces.shape[1]))
    # Spliting training and testing dataset
    X_train, X_test, y_train, y_test = train_test_split(faces, ids, test_size=0.25, random_state=42)
    #print ">>>>>>>>>>>>>>> "+str(y_test.size)
    n_classes = y_test.size
    target_names = ['Manjil Tamang', 'Marina Tamang','Anmol Chalise']
    n_components = 15
    print("Extracting the top %d eigenfaces from %d faces"
          % (n_components, X_train.shape[0]))
    t0 = time()

    pca = PCA(n_components=n_components, svd_solver='randomized',whiten=True).fit(X_train)

    print("done in %0.3fs" % (time() - t0))
    eigenfaces = pca.components_.reshape((n_components, h, w))
    print("Projecting the input data on the eigenfaces orthonormal basis")
    t0 = time()
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)
    print("done in %0.3fs" % (time() - t0))

    # #############################################################################
    # Train a SVM classification model

    print("Fitting the classifier to the training set")
    t0 = time()
    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
                  'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
    clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
    clf = clf.fit(X_train_pca, y_train)
    print("done in %0.3fs" % (time() - t0))
    print("Best estimator found by grid search:")
    print(clf.best_estimator_)

    # #############################################################################
    # Quantitative evaluation of the model quality on the test set

    print("Predicting people's names on the test set")
    t0 = time()
    y_pred = clf.predict(X_test_pca)
    print("Predicted labels: ",y_pred)
    print("done in %0.3fs" % (time() - t0))

    print(classification_report(y_test, y_pred, target_names=target_names))
    # print(confusion_matrix(y_test, y_pred, labels=range(n_classes)))

    # #############################################################################
    # Qualitative evaluation of the predictions using matplotlib

    def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
        """Helper function to plot a gallery of portraits"""
        plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
        plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
        for i in range(n_row * n_col):
            plt.subplot(n_row, n_col, i + 1)
            plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
            plt.title(titles[i], size=12)
            plt.xticks(())
            plt.yticks(())

    # plot the gallery of the most significative eigenfaces
    eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
    plot_gallery(eigenfaces, eigenface_titles, h, w)
    # plt.show()

    '''
        -- Saving classifier state with pickle
    '''
    svm_pkl_filename ='ml/serializer/svm_classifier.pkl'
    # Open the file to save as pkl file
    svm_model_pkl = open(svm_pkl_filename, 'wb')
    pickle.dump(clf, svm_model_pkl)
    # Close the pickle instances
    svm_model_pkl.close()



    pca_pkl_filename ='ml/serializer/pca_state.pkl'
    # Open the file to save as pkl file
    pca_pkl = open(pca_pkl_filename, 'wb')
    pickle.dump(pca, pca_pkl)
    # Close the pickle instances
    pca_pkl.close()

    plt.show()

    return redirect('/')

@app.route("/detectImage")
def detectImage():
    userImage = request.FILES['userImage']

    svm_pkl_filename ='ml/serializer/svm_classifier.pkl'

    svm_model_pkl = open(svm_pkl_filename, 'rb')
    svm_model = pickle.load(svm_model_pkl)
    #print "Loaded SVM model :: ", svm_model

    pca_pkl_filename ='ml/serializer/pca_state.pkl'

    pca_model_pkl = open(pca_pkl_filename, 'rb')
    pca = pickle.load(pca_model_pkl)
    #print pca

    '''
    First Save image as cv2.imread only accepts path
    '''
    im = Image.open(userImage)
    #im.show()
    imgPath ='ml/uploadedImages/'+str(userImage)
    im.save(imgPath, 'JPEG')

    '''
    Input Image
    '''
    try:
        inputImg = casc.facecrop(imgPath)
        inputImg.show()
    except :
        print("No face detected, or image not recognized")
        return redirect('/error_image')

    imgNp = np.array(inputImg, 'uint8')
    #Converting 2D array into 1D
    imgFlatten = imgNp.flatten()
    #print imgFlatten
    #print imgNp
    imgArrTwoD = []
    imgArrTwoD.append(imgFlatten)
    # Applyting pca
    img_pca = pca.transform(imgArrTwoD)
    #print img_pca

    pred = svm_model.predict(img_pca)
    print(svm_model.best_estimator_)
    print (pred[0])

    return redirect('records/details/'+str(pred[0]))

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")

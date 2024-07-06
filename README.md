# Resume pdf_to_json
Good Evening everyone Just Created a code where it converts the Resume content pdf to json file.
Feel free to checkout the code. :) 

What was the goal behind making this project??

The goal is to be able to quickly extract all the available information in the document to a python dictionary.

What all does it Extracts?

* Document metadata : summary, experience, education, skills, projects, campus engagement, course completion, awards and achievements.
* Page texts (in Unicode, when availabe, no OCR here) and text attributes (fonts etc)

Modules:
* fitz 
* json
## Output:

```json
{
    "other": [
        "Tanishque Kumar",
        "7995738255 | tanishqkumar678@gmail.com | linkedin.com-tanishq-kumar | github.com-Tani2189"
    ],
    "education": [
        "SRM University",
        "Kathakulanthur, Chennai",
        "B.Tech in Computer Science and Engineering",
        "2021 – 2025",
        "TECHNICAL SKILLS",
        "Releavent Coursework: Machine Learning, Deep Learning, Statistics, ,Big Data Analytics,Probability and Discrete Mathematics,Data",
        "Structures and Algorithms, Quantum Computation,Devops and CICD Pipelines.",
        "Programming Languages: Python, C++, SQL, MATLAB",
        "Frameworks: TensorFlow, PyTorch, Keras, Bootstrap",
        "Libraries & Tools: NumPy, Pandas, Scikit-learn, OpenCV, NLTK, Git, Docker, AWS"
    ],
    "projects": [
        "LipSyncInsight",
        "Python,Tensorﬂow-Keras,LSTM,BI-LSTM model",
        "Deep Learning",
        "• Developed a web app in which it can read Lip of the human being and predict what is it trying to say.",
        "• for deploying as a webapp I used streamlit.",
        "Super Resolution of Image using SRGAN",
        "Python,OpenCV,Transfer Learning, Tensorﬂow,CNN",
        "Deep Learning",
        "• The SRGAN (Super-Resolution Generative Adversarial Network) model was used to increase the resolution of the given",
        "low-resolution images to a decent resolution. SRGAN is a powerful deep learning technique that has been widely used for image",
        "super-resolution tasks.",
        "• The SRGAN model was trained using the transfer learning concept, where the VGG19 model was used as the feature extractor, and",
        "the remaining layers of the SRGAN model were trained on the speciﬁc task of image super-resolution. This approach allowed the",
        "model to beneﬁt from the rich feature representations learned by the VGG19 model, while also ﬁne tuning the model to the speciﬁc",
        "task at hand.",
        "Quantum Vault",
        "Python, Machine Learning, Quantum Computation, Quantum Key Distribution",
        "Quantum Computing",
        "• Engineered an anomaly detection software powered with Quantum Machine learning and Artiﬁcial Intelligence poised to redeﬁne",
        "how organizations handle sensitive and conﬁdential information, ensuring both security and efﬁciency.",
        "• Clasped a groundbreaking ﬁntech pursuits that was developed over the time to enhance the data catastrophe and provide over 4",
        "layers of security in the form of superposition, Hilbert Spaces, homomorphic encryption and Quantum Key distribution (QKD) and",
        "achieved data contamination value of 0.01 and test loss of 2.687 with a successful implementation of ZZ Feature Maps.",
        "Cancer Image Classiﬁer Using HQCNN",
        "Python, Machine Learning, CNN, QCNN, Perceptron, PyTorch",
        "Deep Learning and Quantum Machine Learning",
        "• Developed a novel Hybrid Quantum Convolutional Neural Network (HQCNN) model for the classiﬁcation of esophageal cancer",
        "images.",
        "• Integration of parameterized quantum circuits into the convolutional and pooling layers to leverage quantum computing’s unique",
        "capabilities for feature extraction and dimensionality reduction.",
        "• Achieving an impressive classiﬁcation accuracy of 99.82 percentage on the esophageal cancer image dataset, outperforming a",
        "conventional CNN model."
    ],
    "experience": [
        "Junior Quantum Research Intern",
        "Nov 2022-July 2023",
        "Qkrishi",
        "• During my tenure as a Quantum Research Intern at Qkrishi, a leader in quantum computing applications, contributed to the",
        "research and development team focused on leveraging quantum machine learning algorithms for fraud detection. My work involved",
        "developing and testing novel quantum-inspired approaches to improve the accuracy and efﬁciency of fraud detection systems.",
        "• Deployed and evaluated various quantum machine learning algorithms, such as Quantum Support Vector Machine (QSVM) and",
        "Variational Quantum Classiﬁer(VQC), to process complex data and identify fraudulent patterns and even making comparision with",
        "the classical machine learning algorithms like SVM.",
        "• During my tenure as a Quantum Research Intern at Qkrishi, I was recognized for my innovative contributions and strong",
        "performance. As a result, I received a letter of recommendation from the organization, afﬁrming my skills and potential in the ﬁeld",
        "of quantum computing."
    ],
    "awards and achievements": [
        "• Runner up in Leap’24 Ideathon+hackathon conducted by IEEE CS",
        "• Was a part of Samsung Prism and Contributed with RD team of Samsung on Multimodal Emotional Gesture Recognition by facial",
        "expressions, voice intonations and human gestures. Implemented model using Python and Deep Learning Concepts",
        "• Received a Certiﬁcate of Appreciation at Felicitation Event conducted by SRMIST for securing an internship, recognizing dedication",
        "and hard work in advancing professional development.",
        "• Was an AI/ML Mentor at Quantathon 1.0 conducted by Quantum Computing Club SRM",
        "• Contributing in National Quantum Mission under a Concerned faculty."
    ],
    "campus engagement": [
        "President",
        "Quantum Computing Club SRM",
        "• Led the Quantum Computing Club, growing membership and fostering a collaborative environment for students passionate about",
        "quantum technologies.",
        "• Planned, and directed workshops on quantum computing highlights to further knowledge regarding quantum principles which are",
        "held by experts in the industry.",
        "• Worked with university departments to receive sponsorships and other resources, expanding the club’s events and outreach",
        "efforts.",
        "ML Lead",
        "Swift Coding Club SRM",
        "• Led innovative projects at Swift Coding Club, seamlessly merging theoretical knowledge with practical applications. I navigated",
        "the club’s focus on enhancing comprehension of machine learning and deep learning concepts, reﬁning both technical prowess and",
        "leadership acumen."
    ],
    "course completion": [
        "• Recently completed a course on Advanced Machine Learning on Google Cloud Specialization offered by Google on Coursera.",
        "• Last Summer attended IBM Qiskit Summer School 2023 lauched by IBM Qiskit and was awarded by a Certiﬁcate of Excellance.",
        "• Completed a AWS Machine Learnig Course offered by Amazon AWS."
    ]
}
```


* By the way the output out here is my resume.
* Thanks!

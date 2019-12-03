# Window-Counter_Object-Detection
## Implemeneting a web application using neural network concepts

### Project Description:

The aim is to automate the stocktaking of buildings. This is needed to initiate new projects or make the calculation of facility management services. A tool that is easy to handle and everyone carries around is the smart phone. So there shall be a web application that takes pictures and collects meta data of the picture as an user input.

### Solution Approach:

#### Architecture

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Architecture.jpg)

#### Use Case Diagram

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Use%20Case%20diagram.jpg)

##### Sequence Diagram

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Sequence%20diagram.jpg)

### Web UI Design

#### Wireframe model

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Wireframe%20model.png)

#### Technologies used:

- HTML

- CSS

- JavaScript

- Bootstrap

- Angular Frame Work

#### Web UI functionality

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Web%20UI%20design_1.png)

### Data Preperation

#### Data Collection

#### Source

- Internet-360 images

- Camera-100 images

#### Data Pre-processing

- Resolution: 800 * 600

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Resized%20image.png)

- Labelling tool: LabelImg

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/labelling.png)

- Labels: {image path, xmin, xmax, ymin, ymax, object_class}

### Model Development

#### Network flow

![Faster R-NN](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Faster%20R-CNN.jpg)

#### Pre-trained CNN

![VGG_16](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/VGG-16.png)

#### Regional Proposal Network

![RPN](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/RPN.png)

- Anchor scaling : 128, 256, 512
- It deploys 9 anchor boxes: 3 different scales at 3 different aspect ratio. 
- Using 9 anchors per location, it generates 2 × 9 objectness scores and 4 × 9 coordinates per location.

#### ROI Pooling

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/ROI%20pooling.png)

- Output of RPN is object proposals with no class
- Problem is classifying these bounding boxes

#### R-CNN

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/R-CNN.png)
- Classify proposals into one of the classes
- Adjust the bounding box

### Model Training

#### Training RPN

Generated Anchor boxes
- Classification (Forground or Background)        
- Regression(BBox fitted/not)
![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/IOU.png)

#### Training Detection Network(R-CNN)

ROI Pooling proposals(softmax layer)

- Classification(Window or not)
- Regression (BBox adjustment)

Loss (0-1) functions: 
            
- RPN regression
- RPN classification
- R-CNN classification
- R-CNN regression

#### Training Results

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Results_1.png)
![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Results_2.png)

#### Testing Results

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Test_image.png)
![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Test_image_result.png)
![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Test_results.png)

### Back-end

#### Tools / Technology

- Python  --  Flask(framework)
- SQLite
- Rest API

### Database Design

![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Database%20design.png)
![](https://github.com/Kamalhsn/Window-Counter_Object-Detection/blob/master/doc_img/Storing%20image%20in%20DB.png)







       



























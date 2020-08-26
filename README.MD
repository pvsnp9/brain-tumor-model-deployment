# Automatice Brain Tumour Segmentation Web application

In this project, Brain MRIs are segmented using Deep learning model using 3D U-net Model. This web application project built using django and deep learning model called 3D-Unet.


## Live Demo on Heroku 
```
[Brain Tumor Segmentation] (https://brain-tumour-segmentation.herokuapp.com/)
```


## Installation and environemnt setup 

* Clone this repository 
```
git clone git@github.com:pvsnp9/brain-tumor-model-deployment.git
```
 * Create environment with pip3 or conda
 ```
conda create --name <env> --file requirements.txt
 ```

```
pip3 install -r requirements.txt
```
inside the environment that you have


### Instruction to Use application

[Models](https://drive.google.com/drive/folders/1JhYFpbRGgvWQaI7QWFRpIlOOZfqnMmIy?usp=sharing) Models that i'have trained. 

Please download those models and put into forllowing directory 
```
static/models
```

* Run locally

```
cd <project_name>
```

then 

```
python manage.py runserver 
```

## Contributing

Self

## Versioning

V 0.0 


## License

This project is licensed under the MIT License. Anybody to use or modify.

## Acknowledgments

* Academic Project | Data Science | UofR
* Will be working on this model in ordee to achieve better result

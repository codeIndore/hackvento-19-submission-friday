# hackvento-19-submission-friday
hackvento-19-submission-friday created by GitHub Classroom

#	About The Project:  
	Capturing a moment in low light is highly challenging due to 
low photon count and low SNR (Signal to noise ratio). Short-exposure images suffer 
from noise, while long exposure can lead to blurry images and is often impractical. So to reduce the noise and make the image achieve high accuracy we made a project Dark vision enhancement  . There are physical means to increase SNR in low light , including  opening the aperture , extending exposure time, and using flash . But each of them is having their own characterstics . 

#	Scope :
	Extent of this project is quite huge. As we know, images from various different sources come noisy and blur in low  light after processing of the image. This technology will help us to sharpen every damaged image. It is having hish scope as in future it would be helpful in self driving cars to reduce low light imaging problem to make driving easy in future. It can also help CCTV and other devices from the secuirity point of view .We thus exclude histogram stretching from pipeline  and optionally apply it as postprocessing.

#	Achieved:
	Generally the ISO of damaged image is found to be 8000 and that too of a denoise image is  406000 . Hence from these figures we can say that what is the difference between these two images is very large.
So by using deep neural networks we trained a model that gives us an enhanced image as an output.
We propose a new image processing pipeline that addresses the challenges of extreme low-light photography via a data-driven approach. Specifically, we train deep neural networks to learn the image processing pipeline for low- light raw data, including color transformations, denoising, noise reduction, and image enhancement. The pipeline is trained end-to-end to avoid the noise amplification and 
error accumulation that characterize traditional camera processing pipelines in this regime.
We systematically analyse key elements of the pipeline. The PNR ratio for this model is 31 .

#	How to Test:
	First of all you need to clone the project either from github or if you are having a copy of the folder 
	Then you need to download the dataset of Sony(25 GB) which contains many dark images. Later you 
	Can run :
			Python 3 manage.py runserver


#	How it Works :
		The input   image is preprocessed using histogram stretching, 
		Then for further processing the image is converted to array (numpy array)
		The image is  passed through Unet and processed for short exposure images(Low ISO) 
		The image is displayed on web page in .png  format 


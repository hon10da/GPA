i=imread('bath image');


i1_gray=rgb2gray(i);
brightness=immultiply(i,1.5);
darker=imdivide(i1,0.6);
hdr=adapthisteq(i1,'clipLimit',0.01);
sharpness=imsharpen(i2);
figure('position',[200,100,1000,800]), 
subplot(2,3,1),imshow(i),title('origenal');
subplot(2,3,2),imshow(sharpness),title('sharpness');
subplot(2,3,3),imshow(brightness),title('brightness');
subplot(2,3,4),imshow(darker),title('darker');
subplot(2,3,5),imshow(hdr),title('hdr');
subplot(2,3,6),imshow(i1_gray),title('i1_gray');

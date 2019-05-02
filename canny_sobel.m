 function canny_sobel(namefile,threshold)
 
   i = imread(namefile);
   I = rgb2gray(i);
   BW1 = edge(I, 'sobel', threshold);
   BW2 = edge(I, 'canny', threshold);
   imwrite(BW1,strcat('sobel_', num2str(threshold), '.png'));
   imwrite(BW2,strcat('canny_', num2str(threshold), '.png'));
   
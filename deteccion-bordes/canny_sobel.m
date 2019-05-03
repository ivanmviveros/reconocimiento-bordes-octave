 function canny_sobel(filename,threshold)
 
   i = imread(filename);
   I = rgb2gray(i);
   BW1 = edge(I, 'sobel', threshold);
   BW2 = edge(I, 'canny', threshold);
   imwrite(BW1,strcat('sobel_', filename, num2str(threshold), '.png'));
   imwrite(BW2,strcat('canny_', filename, num2str(threshold), '.png'));
   
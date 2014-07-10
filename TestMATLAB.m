%Code was copied and edited from MATHWORKS examples
%http://www.mathworks.com/help/images/examples/color-based-segmentation-using-k-means-clustering.html?prodcode=IP&language=en
%Edited by: Andrea Hidalgo
%July 10th, 2014

figure(1)
RGBsample = imread('RGBsample.jpg');
imshow(RGBsample),title('Messier-83'); 
text(size(RGBsample,2),size(RGBsample,1)+15,...
    'WFC3 ERS M83 DATA, http://archive.stsci.edu/prepds/wfc3ers/m83datalist.html',...
    'Fontsize',7,'HorizontalAlignment','right');
cform = makecform('srgb2lab');
lab_RGBsample = applycform(RGBsample,cform);

ab = double(lab_RGBsample(:,:,2:3));
nrows = size(ab,1);
ncols = size(ab,2);
ab = reshape(ab,nrows*ncols,2);

nColors = 3;
% repeat the clustering 3 times to avoid local minima
[cluster_idx, cluster_center] = kmeans(ab,nColors,'distance','sqEuclidean', ...
                                      'Replicates',3);
pixel_labels = reshape(cluster_idx,nrows,ncols);
figure(2)
imshow(pixel_labels,[]), title('image labeled by cluster index');

segmented_images = cell(1,3);
rgb_label = repmat(pixel_labels,[1 1 3]);

for k = 1:nColors
    color = RGBsample;
    color(rgb_label ~= k) = 0;
    segmented_images{k} = color;
end

figure(3)
imshow(segmented_images{1}), title('objects in cluster 1');
figure(4)
imshow(segmented_images{2}), title('objects in cluster 2');
figure(5)
imshow(segmented_images{3}), title('objects in cluster 3');

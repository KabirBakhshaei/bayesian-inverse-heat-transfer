% 3D Scatter Plot Animation 
% This MATLAB script generates a 3D scatter plot animation to visualize
% the true and reconstructed heat flux over time. It loads data from
% specific files, calculates the heat flux reconstruction, and creates an
% animation showing the true and reconstructed heat flux in a 3D plot.
% The animation is saved as '3D Combined scatter plot.avi'.
%
% Please make sure to set the appropriate file paths for data loading.
clc; clearvars; close all;

%cd('/u/k/kbakhsha/ITHACA-FV-KF/tutorials/UQ/07enKFwDF_3dIHTP')
cd('E:\SISSA\000 Ensemble\10 35   Gaussian\Files')

% Load the data for the first animation
gtrue = load('./ITHACAoutput/projection/TrueHeatFlux/HeatFluxTrue_mat.txt'); % [101, 400]
gtrue = gtrue (1:end-1,:);

% Load parameterMean and heatFluxSpaceRBF matrices
parameterMean = load('./ITHACAoutput/reconstruction/parameterMean_mat.txt'); % [25, 100]
heatFluxSpaceRBF = load('./ITHACAoutput/projection/HeatFluxSpaceRBF/heat_flux_space_basis_mat.txt'); % [25, 400]

% Get the dimensions of parameterMean and heatFluxSpaceRBF matrices
[n1, m1] = size(parameterMean); % n1 = 25 (mean/weight), m1 = 100 (times)
[n, m] = size(heatFluxSpaceRBF); % n = 25 (RBF), m = 400 (faces)

% Initialize the out matrix with zeros
out = zeros(m1, m); % (100, 400)

% Perform matrix multiplication and summation
for i = 1:m1 % Loop over times (100 times)
    for j = 1:m % Loop over faces (400 faces)
        out(i, j) = sum(parameterMean(:, i) .* heatFluxSpaceRBF(:, j)); % Matrix multiplication and summation
    end
end


% Load the 'xyz.npy' file
xyz = load('xyz.txt');

% Extract x, y, and z arrays
x = xyz(1:3:end);  % Start at index 1 and take every third element
y = xyz(2:3:end);  % Start at index 2 and take every third element
z = xyz(3:3:end);  % Start at index 3 and take every third element

% Load trueTimeVec_mat.txt
timeInstants = load('./ITHACAoutput/true/trueTimeVec_mat.txt');

% Create a VideoWriter object to save the animation
writerObj = VideoWriter('3D Combined scatter plot.avi', 'Motion JPEG AVI');
writerObj.FrameRate = 30;  % Adjust the frame rate as needed (e.g., 10 frames per second)
writerObj.Quality = 100;   % Set the video quality (maximum quality)
open(writerObj);

% Create a figure for the 3D plots and set it to full screen
fig = figure('Position', get(0, 'ScreenSize'));
%fig = figure('Position', [0, 0, 1930, 1073]); % Set the figure size to 1920x1080

xmin = 0;
xmax = 2;
zmin = 0;
zmax = 1.2;
gtrue_min = min(min(gtrue(:)), min(out(:)));
gtrue_max = max(max(gtrue(:)), max(out(:)));

% Set font size and font type
fontSize = 16;  % Adjust the desired font size
fontType = 'Times New Roman';
fontsize2 = 14;

for i = 1:length(timeInstants)
    % Extract the data for the current time instant
    gtrue_t = gtrue(i, :);
    
    % Create a 3D scatter plot for gtrue on the xz plane
    subplot(1, 2, 1); % Create a subplot for gtrue
    scatter3(x, z, gtrue_t, 'filled');
    
    % Set plot labels and title for gtrue
    xLabelHandle = xlabel('X');
    yLabelHandle = ylabel('Z');
    zLabelHandle = zlabel('True Heat Flux');
    
    titleHandle = title(['True Heat Flux at Time Instant ', num2str(i)]);
    %titleHandle = title(['Time = ', num2str(i*0.2), ' sec']);
    axis([xmin, xmax, zmin, zmax, gtrue_min, gtrue_max]);
  
    set(xLabelHandle, 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
    set(yLabelHandle, 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
    set(zLabelHandle, 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
    set(titleHandle, 'FontSize', fontSize, 'FontName', fontType);

    ax = gca;
    ax.XAxis.FontSize = fontsize2;
    %ax.XAxis.FontWeight = 'bold';
    ax.YAxis.FontSize = fontsize2;
    %ax.YAxis.FontWeight = 'bold';
    ax.ZAxis.FontSize = fontsize2;
    %ax.ZAxis.FontWeight = 'bold';

    grid on
    % Extract the data for the current time instant in the 'out' matrix
    out_t = out(i, :);
    
    % Create a 3D scatter plot for out on the xz plane
    subplot(1, 2, 2); % Create a subplot for 'out'
    scatter3(x, z, out_t, 'filled');
    
    % Set plot labels and title for 'out'  
    xLabelHandle = xlabel('X');
    yLabelHandle = ylabel('Z');
    zLabelHandle = zlabel('Reconstructed Heat Flux');

    titleHandle = title(['Reconstructed Heat Flux at Time Instant ', num2str(i)]);
    %titleHandle = title(['Time = ', num2str(i*0.2), ' sec']);
    axis([xmin, xmax, zmin, zmax, gtrue_min, gtrue_max]);

    set(xLabelHandle, 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
    set(yLabelHandle, 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
    set(zLabelHandle, 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
    set(titleHandle, 'FontSize', fontSize, 'FontName', fontType);

    ax = gca;
    ax.XAxis.FontSize = fontsize2;
    %ax.XAxis.FontWeight = 'bold';
    ax.YAxis.FontSize = fontsize2;
    %ax.YAxis.FontWeight = 'bold';
    ax.ZAxis.FontSize = fontsize2;
    %ax.ZAxis.FontWeight = 'bold';

    grid on

    
    % Capture the frame and add it to the video
    frame = getframe(fig);
    writeVideo(writerObj, frame);

    % Pause to allow time to view the plot (optional)
    pause(0.1);
end

% Close the video file
close(writerObj);

% Display a message indicating that the animation has been saved
disp('Animation saved as "3D Combined scatter plot.avi"');

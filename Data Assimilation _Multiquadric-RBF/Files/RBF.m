clc; clearvars; close all;

% Verify the current directory
cd('/u/k/kbakhsha/ITHACA-FV-KF/tutorials/UQ/07enKFwDF_3dIHTP');
currentDir = pwd;
disp(['Current directory: ' currentDir])

% Load the 'xyz.txt' and 'Temp.txt' file
xyz = load('xyz.txt');
RBFs = load('Temp.txt');

% Extract x, y, and z arrays
X_coordinate = xyz(1:3:end);   %                Start at index 1 and take every third element
m= length(X_coordinate);
Y_coordinate = zeros(m,1);     % xyz(2:3:end);  Start at index 2 and take every third element
Z_coordinate = xyz(3:3:end);   %                Start at index 3 and take every third element

%scatter(X_coordinate, Z_coordinate, markerSize=20, markerColor='k', 'filled', 'LineWidth', lineWidth=2);
scatter(X_coordinate, Z_coordinate, 22, 'k', 'filled', 'LineWidth', 2);
xlabel('X', 'FontSize', 12, 'FontName', 'Times New Roman', 'FontWeight', 'bold');
ylabel('Z', 'FontSize', 12, 'FontName', 'Times New Roman', 'FontWeight', 'bold');
set(gca, 'FontSize', 10);  
set(gca, 'FontWeight', 'bold');
dpi = 400;
print('XZCentersOfFaces.png', '-dpng', ['-r' num2str(dpi)]);


%[Xgrid, Zgrid] = meshgrid(min(X_coordinate):fineGridResolution:max(X_coordinate), min(z_coordinate):fineGridResolution:max(z_coordinate));
[Xgrid, Zgrid] = meshgrid(linspace(min(X_coordinate), max(X_coordinate), 21), linspace(min(Z_coordinate), max(Z_coordinate), 20));
Ygrid = zeros(size(Xgrid)); % Set Y-coordinate to zero for all points

RBFq1 = griddata(X_coordinate, Z_coordinate, RBFs(:,1), Xgrid, Zgrid, 'nearest'); % Use cubic interpolation for smoother contours
RBFq2 = griddata(X_coordinate, Z_coordinate, RBFs(:,2), Xgrid, Zgrid, 'nearest'); % Use cubic interpolation for smoother contours
RBFq3 = griddata(X_coordinate, Z_coordinate, RBFs(:,3), Xgrid, Zgrid, 'nearest'); % Use cubic interpolation for smoother contours
RBFq4 = griddata(X_coordinate, Z_coordinate, RBFs(:,4), Xgrid, Zgrid, 'nearest'); % Use cubic interpolation for smoother contours
RBFq5 = griddata(X_coordinate, Z_coordinate, RBFs(:,5), Xgrid, Zgrid, 'nearest'); % Use cubic interpolation for smoother contours

figure(1)
C1 = surf(Xgrid, Zgrid, RBFq1, 'FaceAlpha',1);
grid on;
fontSize = 12;
fontType = 'Times New Roman'; % Set the desired font type
xlabel('X', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
ylabel('Z', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
zlabel('Gaussian RBF', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold'); % Gaussian Multiquadric
xlim =[0,2];
ylim= [0,1.2];
colormap('jet');   % You can choose different colormaps
%shading interp;   % Interpolated shading for a smoother appearance
% Add a color bar (legend)
CC = colorbar;
CC.FontSize = 10 ;
CC.FontWeight = 'bold';
% Adjust the view angle (optional)
view(45, 30);
dpi = 400;
print('Gaussian1.png', '-dpng', ['-r' num2str(dpi)]);

figure(2)
C2 = surf(Xgrid, Zgrid, RBFq2, 'FaceAlpha',1);
grid on;
fontSize = 12;
fontType = 'Times New Roman'; % Set the desired font type
xlabel('X', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
ylabel('Z', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
zlabel('Gaussian RBF', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold'); % Gaussian Multiquadric
xlim =[0,2];
ylim= [0,1.2];
colormap('jet');   % You can choose different colormaps
%shading interp;   % Interpolated shading for a smoother appearance
% Add a color bar (legend)
CC = colorbar;
CC.FontSize = 10 ;
CC.FontWeight = 'bold';
% Adjust the view angle (optional)
view(45, 30);
dpi = 400;
print('Gaussian2.png', '-dpng', ['-r' num2str(dpi)]);

figure(3)
C3 = surf(Xgrid, Zgrid, RBFq3, 'FaceAlpha',1);
grid on;
fontSize = 12;
fontType = 'Times New Roman'; % Set the desired font type
xlabel('X', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
ylabel('Z', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
zlabel('Gaussian RBF', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold'); % Gaussian Multiquadric
xlim =[0,2];
ylim= [0,1.2];
colormap('jet');   % You can choose different colormaps
%shading interp;   % Interpolated shading for a smoother appearance
% Add a color bar (legend)
CC = colorbar;
CC.FontSize = 10 ;
CC.FontWeight = 'bold';
% Adjust the view angle (optional)
view(45, 30);
dpi = 400;
print('Gaussian3.png', '-dpng', ['-r' num2str(dpi)]);

figure(4)
C4 = surf(Xgrid, Zgrid, RBFq4, 'FaceAlpha',1);
grid on;
fontSize = 12;
fontType = 'Times New Roman'; % Set the desired font type
xlabel('X', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
ylabel('Z', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
zlabel('Gaussian RBF', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold'); % Gaussian Multiquadric
xlim =[0,2];
ylim= [0,1.2];
colormap('jet');   % You can choose different colormaps
%shading interp;   % Interpolated shading for a smoother appearance
% Add a color bar (legend)
CC = colorbar;
CC.FontSize = 10 ;
CC.FontWeight = 'bold';
% Adjust the view angle (optional)
view(45, 30);
dpi = 400;
print('Gaussian4.png', '-dpng', ['-r' num2str(dpi)]);

figure(5)
C5 = surf(Xgrid, Zgrid, RBFq5, 'FaceAlpha',1);
%C.EdgeColor = 'none';
%C.FontSize = 10 ;
%C.FontWeight = 'bold';
grid on;
fontSize = 12;
fontType = 'Times New Roman'; % Set the desired font type
xlabel('X', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
ylabel('Z', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold');
zlabel('Gaussian RBF', 'FontSize', fontSize, 'FontName', fontType, 'FontWeight', 'bold'); % Gaussian Multiquadric
xlim =[0,2];
ylim= [0,1.2];
% Customize the plot as needed (e.g., colormap, shading, lighting, etc.)
colormap('jet'); % You can choose different colormaps
%shading interp;   % Interpolated shading for a smoother appearance
% Add a color bar (legend)
CC = colorbar;
CC.FontSize = 10 ;
CC.FontWeight = 'bold';
% Adjust the view angle (optional)
view(45, 30);
dpi = 400;
print('Gaussian5.png', '-dpng', ['-r' num2str(dpi)]);

%The code is developed by SalimWireless.Com

clc;
clear;
close all;

% Define parameters
M = 16; % Modulation order for 16-QAM
numSymbols = 10000; % Number of symbols to modulate

% Generate random data
data = randi([0 M-1], numSymbols, 1); % Ensure data is a column vector

% Modulate the data using 16-QAM
modData = qammod_custom(data, M);

snrdB = 15;
Y = awgn(modData,snrdB); %received signal

% Plot the constellation of the modulated signal
figure;
subplot(2,1,1);
scatter(real(modData), imag(modData), 'o');
grid on;
xlabel('In-phase');
ylabel('Quadrature');
title('Constellation Diagram of Modulated Signal (16-QAM)');
axis([-1.5 1.5 -1.5 1.5]); % Set axis limits for better visualization

subplot(2,1,2);
scatter(real(Y), imag(Y), 'o');
grid on;
xlabel('In-phase');
ylabel('Quadrature');
title('Constellation Diagram of Noisy Received Signal before demodulation');
axis([-1.5 1.5 -1.5 1.5]); % Set axis limits for better visualization


% Demodulate the received signal
receivedData = qamdemod_custom(modData, M);

% Ensure receivedData is a column vector for comparison
receivedData = receivedData(:);


% Custom 16-QAM Modulation Function
function modData = qammod_custom(data, M)
    % QAMMOD_CUSTOM Modulate data using 16-QAM
    % data - Column vector of integers (each element is between 0 and M-1)
    % M - Modulation order (should be 16 for 16-QAM)
    
    % Check if M is 16
    if M ~= 16
    error('This function is designed for 16-QAM modulation.');
    end
    
    % Define the 16-QAM constellation
    constellation = [-3-3i, -3-1i, -1-3i, -1-1i, ...
    -3+3i, -3+1i, -1+3i, -1+1i, ...
    +3-3i, +3-1i, +1-3i, +1-1i, ...
    +3+3i, +3+1i, +1+3i, +1+1i];
    
    % Normalize constellation
    constellation = constellation / sqrt(mean(abs(constellation).^2)); % Scale to unit average power
    
    % Map data to constellation points
    modData = constellation(data + 1);
end

% Custom 16-QAM Demodulation Function
function demodData = qamdemod_custom(modData, M)
    % QAMDEMOD_CUSTOM Demodulate data using 16-QAM
    % modData - Column vector of complex numbers (modulated symbols)
    % M - Modulation order (should be 16 for 16-QAM)
    
    % Check if M is 16
    if M ~= 16
    error('This function is designed for 16-QAM demodulation.');
    end
    
    % Define the 16-QAM constellation
    constellation = [-3-3i, -3-1i, -1-3i, -1-1i, ...
    -3+3i, -3+1i, -1+3i, -1+1i, ...
    +3-3i, +3-1i, +1-3i, +1-1i, ...
    +3+3i, +3+1i, +1+3i, +1+1i];
    
    % Normalize constellation
    constellation = constellation / sqrt(mean(abs(constellation).^2)); % Scale to unit average power
    
    % Ensure modData is a column vector
    modData = modData(:);
    
    % Compute the distances from each modData point to all constellation points
    numSymbols = length(modData);
    numConstellations = length(constellation);
    distances = zeros(numSymbols, numConstellations);
    for k = 1:numConstellations
    distances(:, k) = abs(modData - constellation(k)).^2;
    end
    
    % Find the closest constellation point for each modData point
    [~, demodData] = min(distances, [], 2);
    
    % Convert to zero-based index
    demodData = demodData - 1;
end

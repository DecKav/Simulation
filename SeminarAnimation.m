clc, clear all, close all;
hold on;
axis([0, 60, 0, 20])
% Create a scatter plot where the area of the marker is 50. Store the handle to the plot
% in the variable hscatter so we can update the position inside of the loop

pick1 = scatter(10, 5, 400, 'g', 'MarkerFaceColor', 'g');
pick2 = scatter(10, 10, 400, 'g', 'MarkerFaceColor', 'g');

goods1 = scatter(30, 5, 400, 'm', 'MarkerFaceColor', 'm');
goods2 = scatter(30, 10, 400, 'm', 'MarkerFaceColor', 'm');
goods3 = scatter(40, 5, 400, 'm', 'MarkerFaceColor', 'm');
goods4 = scatter(40, 10, 400, 'm', 'MarkerFaceColor', 'm');
goods5 = scatter(50, 5, 400, 'm', 'MarkerFaceColor', 'm');
goods6 = scatter(50, 10, 400, 'm', 'MarkerFaceColor', 'm');

charge1 = scatter(10, 15, 400, 'b', 'MarkerFaceColor', 'b');

car1 = scatter(1, 1, 50, 'r', 'MarkerFaceColor', 'r');

t1 = linspace(0,30);
x1 = t1;
y1 = t1/6;

t2 = linspace(30, 10);
x2 = t2;
y2 = y1(end) + 0*t2;

t3 = linspace(10,30);
x3 = t3;
y3 = y2(end) + 0*t2;

for k = 1:length(t1)
    % Update the location of the scatter plot
    set(car1, 'XData', x1(k), ...    % Set the X Position of the circle to x(k)
                  'YData', y1(k))        % Set the Y Position of the circle to y(k)

    % Refresh the plot
    drawnow
    pause(0.05)
end

pause(1)

for k = 1:length(t2)
    % Update the location of the scatter plot
    set(car1, 'XData', x2(k), ...    % Set the X Position of the circle to x(k)
                  'YData', y2(k))        % Set the Y Position of the circle to y(k)

    % Refresh the plot
    drawnow
    pause(0.05)
end

pause(1)

for k = 1:length(t3)
    % Update the location of the scatter plot
    set(car1, 'XData', x3(k), ...    % Set the X Position of the circle to x(k)
                  'YData', y3(k))        % Set the Y Position of the circle to y(k)

    % Refresh the plot
    drawnow
    pause(0.05)
end
clc, clear all, close all;
hold on;
axis([0, 60, 0, 20])

pick1 = scatter(10, 5, 400, 'g', 'MarkerFaceColor', 'g');
goods1 = scatter(30, 5, 400, 'r', 'MarkerFaceColor', 'r');
charge1 = scatter(10, 15, 400, 'c', 'MarkerFaceColor', 'c');
car = scatter(1000, 1000, 50, 'k', 'MarkerFaceColor', 'k');

pick2 = scatter(10, 10, 400, 'g', 'MarkerFaceColor', 'g');

goods2 = scatter(30, 10, 400, 'r', 'MarkerFaceColor', 'r');
goods3 = scatter(40, 5, 400, 'r', 'MarkerFaceColor', 'r');
goods4 = scatter(40, 10, 400, 'r', 'MarkerFaceColor', 'r');
goods5 = scatter(50, 5, 400, 'r', 'MarkerFaceColor', 'r');
goods6 = scatter(50, 10, 400, 'r', 'MarkerFaceColor', 'r');

car1 = scatter(1, 1, 50, 'k', 'MarkerFaceColor', 'k');

t1 = linspace(0,30);
x1 = t1;
y1 = t1/6;

t2 = linspace(30, 10);
x2 = t2;
y2 = y1(end) + 0*t2;

t3 = linspace(10,30);
x3 = t3;
y3 = y2(end) + 0*t2;

%(30, 5) -> (10, 15)
t4 = linspace(30, 10);
x4 = t4;
y4 = t3/2;

legend('Pickers', 'Goods', 'Charger', 'Car')
status = 'Moving to goods';

for k = 1:length(t1)
    % Update the location of the scatter plot
    set(car1, 'XData', x1(k), ...    % Set the X Position of the circle to x(k)
                  'YData', y1(k))        % Set the Y Position of the circle to y(k)

    % Refresh the plot
    message = text(x1(k)-5, y1(k)+1, status);
    drawnow
    pause(0.002)
    delete(message)
end

delete(message)
status = 'Collecting goods';
message = text(x1(k)-5, y1(k)+1, status);
drawnow
pause(1)
status = 'Transporting goods';

for k = 1:length(t2)
    delete(message)
    % Update the location of the scatter plot
    set(car1, 'XData', x2(k), ...    % Set the X Position of the circle to x(k)
                  'YData', y2(k))        % Set the Y Position of the circle to y(k)

    % Refresh the plot
    message = text(x2(k)-5, y2(k)+1, status);
    drawnow
    pause(0.001)
    delete(message)
end

status = 'Waiting for picking';
message = text(x2(k)-5, y2(k)+1, status);
pause(1)
delete(message)
status = 'Transporting goods';

for k = 1:length(t3)
    % Update the location of the scatter plot
    set(car1, 'XData', x3(k), ...    % Set the X Position of the circle to x(k)
                  'YData', y3(k))        % Set the Y Position of the circle to y(k)

    % Refresh the plot
    message = text(x3(k)-5, y3(k)+1, status);
    drawnow
    pause(0.001)
    delete(message)
end

status = 'Returning goods';
message = text(x3(k)-5, y3(k)+1, status);
pause(1)
delete(message)
status = 'Move to charge';

for k = 1:length(t4)
    % Update the location of the scatter plot
    set(car1, 'XData', x4(k), ...    % Set the X Position of the circle to x(k)
                  'YData', y4(k))        % Set the Y Position of the circle to y(k)

    % Refresh the plot
    message = text(x4(k)-5, y4(k)+1, status);
    drawnow
    pause(0.002)
    delete(message)
end

status = 'Charging';
message = text(x4(k)-3, y4(k)+1, status);
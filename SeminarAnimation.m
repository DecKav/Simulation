clc, clear all, close all;

hold on;
axis([0, 60, 0, 20])
axis off

pick1 = scatter(10, 5, 400, 'g', 'MarkerFaceColor', 'g');
goods = scatter(10000, 100000, 400, 'r', 'MarkerFaceColor', 'r');
goods1 = rectangle('Position', [27.5, 3.75, 5, 2.5], 'EdgeColor', 'k', 'FaceColor', 'r');
charge1 = scatter(10, 10, 400, 'c', 'MarkerFaceColor', 'c');
car = scatter(1000, 1000, 50, 'k', 'MarkerFaceColor', 'k');

pick2 = scatter(10, 7.5, 400, 'g', 'MarkerFaceColor', 'g');

% goods2 = scatter(30, 10, 400, 'r', 'MarkerFaceColor', 'r');
% goods3 = scatter(40, 5, 400, 'r', 'MarkerFaceColor', 'r');
% goods4 = scatter(40, 10, 400, 'r', 'MarkerFaceColor', 'r');
% goods5 = scatter(50, 5, 400, 'r', 'MarkerFaceColor', 'r');
% goods6 = scatter(50, 10, 400, 'r', 'MarkerFaceColor', 'r');

goods2 = rectangle('Position', [27.5, 6.25, 5, 2.5], 'EdgeColor', 'k', 'FaceColor', 'r');
goods3 = rectangle('Position', [32.5, 3.75, 5, 2.5], 'EdgeColor', 'k', 'FaceColor', 'r');
goods4 = rectangle('Position', [32.5, 6.25, 5, 2.5], 'EdgeColor', 'k', 'FaceColor', 'r');
goods5 = rectangle('Position', [37.5, 3.75, 5, 2.5], 'EdgeColor', 'k', 'FaceColor', 'r');
goods6 = rectangle('Position', [37.5, 6.25, 5, 2.5], 'EdgeColor', 'k', 'FaceColor', 'r');

car1 = scatter(1, 1, 50, 'k', 'MarkerFaceColor', 'k');
car2 = scatter(1, 1, 50, 'k', 'MarkerFaceColor', 'k');

t1 = linspace(0,30);
x1 = t1;
y1 = t1/6;
y1b = t1/4;

t2 = linspace(30, 10);
x2 = t2;
y2 = y1(end) + 0*t2;
y2b = y2+2.5;

t3 = linspace(10,30);
x3 = t3;
y3 = y1(end) + 0*t2;
y3b = y3+2.5;

%(30, 5) -> (10, 15)
t4 = linspace(30, 10);
x4 = t4;
x4b = linspace(30, 35, 100);
y4 = linspace(15,30)/3;
y4b = y3b(end)+0*x4b;

t5 = linspace(35,10);
x5 = t5;
y5 = y4b(end)+0*x5;

t6 = linspace(10,35);
x6 = t6;
y6 = y5(end)+0*x6;

legend('Pickers', 'Goods', 'Charger', 'Car')
status = 'Moving to goods';

for k = 1:length(t1)
    % Update the location of the scatter plot
    set(car1, 'XData', x1(k), ...    % Set the X Position of the circle to x(k)
                  'YData', y1(k))        % Set the Y Position of the circle to y(k)
    
    set(car2, 'XData', x1(k), 'YData', y1b(k))
              
    % Refresh the plot
    message = text(x1(k)-5, y1(k)+1, status);
    message2 = text(x1(k)-5, y1b(k)+1, status);
    drawnow

    delete(message)
    delete(message2)
end

delete(message)
delete(message2)
status = 'Collecting goods';  
message = text(x1(k)-5, y1(k)+1, status);
message2 = text(x1(k)-5, y1b(k)+1, status);
drawnow
pause(1)
%goods1 = rectangle('Position', [27.5, 3.75, 5, 2.5], 'EdgeColor', 'k');
set(goods1, 'FaceColor', 'w')
set(car1, 'MarkerFaceColor', 'r')
set(goods2, 'FaceColor', 'w')
set(car2, 'MarkerFaceColor', 'r')
status = 'Transporting goods';

delete(message)
delete(message2)

for k = 1:length(t2)
    % Update the location of the scatter plot
    set(car1, 'XData', x2(k), ...    % Set the X Position of the circle to x(k)
                  'YData', y2(k))        % Set the Y Position of the circle to y(k)
    set(car2, 'XData', x2(k), 'YData', y2b(k))
              
    % Refresh the plot
    message = text(x2(k)-5, y2(k)+1, status);
    message2 = text(x2(k)-5, y2b(k)+1, status);
    drawnow

    delete(message)
    delete(message2)
end

status = 'Waiting for picking';
message = text(x2(k)-5, y2(k)+1, status);
message2 = text(x2(k)-5, y2b(k)+1, status);
pause(1)
delete(message)
delete(message2)
status = 'Transporting goods';

for k = 1:length(t3)
    % Update the location of the scatter plot
    set(car1, 'XData', x3(k), ...    % Set the X Position of the circle to x(k)
                  'YData', y3(k))        % Set the Y Position of the circle to y(k)
    set(car2, 'XData', x3(k), 'YData', y3b(k))
    % Refresh the plot
    message = text(x3(k)-5, y3(k)+1, status);
    message2 = text(x3(k)-5, y3b(k)+1, status);
    drawnow

    delete(message)
    delete(message2)
end

status = 'Returning goods';
message = text(x3(k)-5, y3(k)+1, status);
message2 = text(x3(k)-5, y3b(k)+1, status);
pause(1)
delete(message)
delete(message2)
set(goods1, 'FaceColor', 'r')
set(car1, 'MarkerFaceColor', 'k')
set(goods2, 'FaceColor', 'r')
set(car2, 'MarkerFaceColor', 'k')
status = 'Move to charge';
status2 = 'Moving to goods';

for k = 1:length(t4)
    % Update the location of the scatter plot
    set(car1, 'XData', x4(k), ...    % Set the X Position of the circle to x(k)
                  'YData', y4(k))        % Set the Y Position of the circle to y(k)
    set(car2, 'XData', x4b(k), 'YData', y4b(k))
    % Refresh the plot
    message = text(x4(k)-5, y4(k)+1, status);
    message2 = text(x4b(k)-5, y4b(k)+1, status2);
    drawnow
    delete(message)
    delete(message2)
end

status = 'Charging';
status2 = 'Collecting goods';
message = text(x4(k)-3, y4(k)+1, status);
message2 = text(x4b(k)-5, y4b(k)+1, status2);
pause(1)
delete(message2)
set(goods4, 'FaceColor', 'w')
set(car2, 'MarkerFaceColor', 'r')
drawnow

for k = 1:length(t5)
    set(car2, 'XData', x5(k), 'YData', y5(k));
    message2 = text(x5(k)-5, y5(k)+1, status2);
    drawnow
    delete(message2)
end

status2 = 'Waiting for picking';
message2 = text(x5(k)-5, y5(k)+1, status2);
pause(1)
delete(message2)
status2 = 'Transporting goods';

for k = 1:length(t6)
    set(car2, 'XData', x6(k), 'YData', y6(k));
    message2 = text(x6(k)-5, y6(k)+1, status2);
    drawnow
    delete(message2)
end

status2 = 'Returning goods';
message2 = text(x6(k)-5, y6(k)+1, status2);
pause(1)
delete(message2)
set(goods4, 'FaceColor', 'r')
set(car2, 'MarkerFaceColor', 'k')
drawnow
status2 = 'Moving to idle';

t7 = linspace(7.5, 10);
x7 = linspace(10, 15);
x7b = x6(end) + 0*t7;
y7 = 10+0*t7;
y7b = t7;

delete(message)
delete(message2)

for k = 1:length(t7)
    set(car1, 'XData', x7(k), 'YData', y7(k));
    set(car2, 'XData', x7b(k), 'YData', y7b(k));
    message = text(x7(k)-5, y7(k)+1, status2);
    message2 = text(x7b(k)-5, y7b(k)+1, status2);
    drawnow
    delete(message)
    delete(message2)
end

status = 'Idle';
message = text(x7(k)-2, y7(k)+1, status);
message2 = text(x7b(k)-2, y7b(k)+1, status);


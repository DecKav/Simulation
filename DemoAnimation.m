clc, clear all, close all;

hold on;
axis([-0.1, 1.1, -0.1, 1.1])

pick = scatter(0, 1, 500, 'g', 'MarkerFaceColor', 'g');
goods = scatter(0, 0, 500, 'r', 'MarkerFaceColor', 'r');
charge = scatter(1, 0, 500, 'c', 'MarkerFaceColor', 'c');
car1 = scatter(0, 0, 100, 'k', 'MarkerFaceColor', 'k');
car2 = scatter(0, 0, 100, 'k', 'MarkerFaceColor', 'k');
car3 = scatter(0, 0, 100, 'k', 'MarkerFaceColor', 'k');
car4 = scatter(0, 0, 100, 'k', 'MarkerFaceColor', 'k');
car5 = scatter(0, 0, 100, 'k', 'MarkerFaceColor', 'k');

steps = csvread('animation_steps.csv');
legend('Picker', 'Goods', 'Charger', 'Car', 'Location', 'southoutside', 'Orientation', 'horizontal')

for i = 1:size(steps, 1)
    message = text(0.8, 1, ['Time step: ', num2str(i)]);
    message2 = text(0.8, 0.95, 'Processing Car: 1'); 
    if (get(car1, 'XData') ~= steps(i, 1))
        set(car1, 'XData', 0.5)
        drawnow
        pause(0.2)
        set(car1, 'XData', steps(i, 1), 'YData', steps(i, 2))
    elseif (get(car1, 'YData') ~= (steps(i, 2)))
        set(car1, 'YData', 0.5)
        drawnow
        pause(0.2)
        set(car1, 'XData', steps(i, 1), 'YData', steps(i, 2))
    end
    drawnow
    pause(0.1)
    delete(message2)
    
    message2 = text(0.8, 0.95, 'Processing Car: 2'); 
    if (get(car2, 'XData') ~= steps(i, 3))
        set(car2, 'XData', 0.5)
        drawnow
        pause(0.2)
        set(car2, 'XData', steps(i, 3), 'YData', steps(i, 4))
    elseif (get(car2, 'YData') ~= (steps(i, 4)))
        set(car2, 'YData', 0.5)
        drawnow
        pause(0.2)
        set(car2, 'XData', steps(i, 3), 'YData', steps(i, 4))
    end
    drawnow
    pause(0.1)
    delete(message2)
    
    message2 = text(0.8, 0.95, 'Processing Car: 3'); 
    if (get(car3, 'XData') ~= steps(i, 5))
        set(car3, 'XData', 0.5)
        drawnow
        pause(0.2)
        set(car3, 'XData', steps(i, 5), 'YData', steps(i, 6))
    elseif (get(car3, 'YData') ~= (steps(i, 6)))
        set(car3, 'YData', 0.5)
        drawnow
        pause(0.2)
        set(car3, 'XData', steps(i, 5), 'YData', steps(i, 6))
    end
    drawnow
    pause(0.1)
    delete(message2)
    
    message2 = text(0.8, 0.95, 'Processing Car: 4'); 
    if (get(car4, 'XData') ~= steps(i, 7))
        set(car4, 'XData', 0.5)
        drawnow
        pause(0.2)
        set(car4, 'XData', steps(i, 7), 'YData', steps(i, 8))
    elseif (get(car3, 'YData') ~= (steps(i, 8)))
        set(car4, 'YData', 0.5)
        drawnow
        pause(0.2)
        set(car3, 'XData', steps(i, 7), 'YData', steps(i, 8))
    end
    drawnow
    pause(0.1)
    delete(message2)
    
    message2 = text(0.8, 0.95, 'Processing Car: 5'); 
    if (get(car5, 'XData') ~= steps(i, 9))
        set(car5, 'XData', 0.5)
        drawnow
        pause(0.2)
        set(car5, 'XData', steps(i, 9), 'YData', steps(i, 10))
    elseif (get(car5, 'YData') ~= (steps(i, 10)))
        set(car5, 'YData', 0.5)
        drawnow
        pause(0.2)
        set(car5, 'XData', steps(i, 9), 'YData', steps(i, 10))
    end
    drawnow
    pause(0.1)
    delete(message2)
    
    pause(0.4)
    delete(message)
end







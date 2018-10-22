N = 24;
Nc = 5;
i = 1;
Q0(1) = 100*Nc; %Initial Charge
J0(1) = 0; %Initial Jobs
w = randi([0 10], N, 1);
x0 = [2 3]; %2 cars each
Aq = [-1 0; 0 -1; -20 -20]; %must be positive, must not lose too much charge
bq = [0; 0; Q0(i, 1)];
Aj = [-1 0; 0 -1]; 
bj = [0; 0];
Aeq = [1, 1]; %Cars must add to total
beq = Nc;

for i = 1:N
    Q = @(u)(-Q0(i) - 2*u(1) + 8*u(2)); %Inverted to maximise
    J = @(u)(J0(i) + w(i) - 8*u(2) + 0*u(1));
    QJ = @(u) Q(u) + J(u);
    
    x(i, :) = fmincon(QJ, x0, Aq, bq, Aeq, beq);
    q(i, :) = fmincon(Q, x0, Aq, bq, Aeq, beq);
    j(i, :) = fmincon(J, x0, Aq, bq, Aeq, beq);
    Q0(i+1) = round(-1*Q(x));
    J0(i+1) = round(J(x));
end
disp(x)

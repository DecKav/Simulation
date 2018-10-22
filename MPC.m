A = eye(2);
B = [2 5; 0 -5];
C = [0; 1];
D = [1 0]; 

Nc = 1;
Np = 16;

[Phi_Phi,Phi_F,Phi_R,A_e, B_e,C_e] = mpcgain(A, B, C, 


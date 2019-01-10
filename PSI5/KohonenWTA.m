close all; clear all; clc;

%Dane wejœciowe
Input = open('iris_dataset.dat');
size(Input);
plot(Input(1, :), Input(2, :),Input(3, :),Input(4, :));
hold on; grid on;

%Parametry sieci
dimensions = [10 10]; 
coverSteps = 100; 
initNeighbor = 0; 
topologyFcn = 'hextop';
distanceFcn = 'dist'; 

%Tworzni sieci 
net = selforgmap(dimensions, coverSteps, initNeighbor, topologyFcn, distanceFcn);
net.trainParam.epochs = 500;

%Terning sieci 
[net, tr] = train(net, Output);
y = net(Output);
grid on
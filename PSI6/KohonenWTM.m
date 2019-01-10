close all; clear all; clc;

%Dane 
       %A B C D E F G H I J K L N O P R S T U Y
Input= [0 1 0 1 1 1 0 1 1 1 1 1 1 0 1 1 0 1 1 1;
        1 1 1 1 1 1 1 0 0 1 0 0 0 1 1 1 1 1 0 0;
        1 1 1 1 1 1 1 0 0 1 0 0 0 1 1 1 1 1 0 1;
        0 0 1 0 1 1 1 1 0 1 1 0 1 0 0 0 1 0 1 0;
        1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 0 1 1;
        0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0;
        0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1;
        1 1 0 1 0 0 0 1 0 1 0 0 1 1 1 1 0 0 1 0;
        1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 0 1 0;
        1 1 0 0 1 1 0 1 0 0 1 0 0 0 1 1 1 1 0 1;
        1 1 0 0 1 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0;
        1 0 0 1 0 0 1 1 0 1 0 0 1 1 0 0 0 0 1 0;
        1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 0 1 0;
        0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1;
        0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0;
        1 1 0 1 0 0 1 1 0 1 0 0 1 1 0 0 1 0 1 0;
        1 1 1 1 1 1 0 1 1 0 1 1 1 0 1 1 1 0 0 0;
        0 1 1 1 1 0 1 0 0 0 0 1 0 1 0 0 1 1 1 1;
        0 1 1 1 1 0 1 0 0 0 0 1 0 1 0 0 1 0 1 0;
        1 0 1 0 1 0 1 1 0 1 1 1 1 0 0 1 0 0 0 0;
        ];
 
%Parametry sieci
 dimensions = [4 5];
coverSteps = 100;
initNeighbor = 1;
topologyFcn = 'gridtop';
distanceFcn = 'dist';

%Stworzenie sieci
net = selforgmap(dimensions,coverSteps,initNeighbor,topologyFcn,distanceFcn);

%trenig sieci
net.trainFcn = 'trainbu';
net.trainParam.epochs = 2000;
[net,tr] = train(net,iData);

%symulacja wyników
y = net(Input);

%tworzenie wykrsów
plotsompos(net,Input);
grid on



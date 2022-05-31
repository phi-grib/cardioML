%     Copyright (C) 2022 Jordi Llopis. Contact: jorllolo@etsii.upv.es

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% This script generates KrKsNaL matrix
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Kr=[-3:0.1:2.5]; % Possible input values for Kr
Ks=[-3:0.1:2.5]; % Possible input values for Ks
NaL=[-3:0.1:2.5]; % Possible input values for NaL

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
inputs=[];
for i = 1:length (NaL)
    for j= 1:length (Ks)
       for k= 1:length (Kr)
            inputs = [inputs; Kr(k) Ks(j) NaL(i)]; % Generate input data
        end
    end
end
%% 
myCluster=parcluster('local');
tic
disp(datetime)
poolobj = gcp('nocreate');
if isempty(poolobj)
    poolobj = parpool(myCluster.NumWorkers);
end
poolobj.IdleTimeout= 120;
%%
parfor i = 1:size(inputs,1)
    Kr_effect = 1/(1+10^(inputs(i,1))); 
    Ks_effect = 1/(1+10^(inputs(i,2))); 
    NaL_effect = 1/(1+10^(inputs(i,3)));

    [time,X,IsJs] = runORdmD(Kr_effect, Ks_effect, NaL_effect, 2); % Running electrophysiological simulation
    [~,~,~,~,~,EADs1]=APD(time{1,1},X{1,1}(:,1),90); % Detecting Repolarization Abnormalities in penultimate beat
    [APD90(i,1),~,~,~,~,EADs2]=APD(time{2,1},X{2,1}(:,1),90); % Detecting Repolarization Abnormalities in the last beat and measuring APD90
    EADs(i,1)=max([EADs1; EADs2]);
end
delete(poolobj)

MatrixKrKsNaL=[inputs APD90 EADs]; % Create the matrix
save('MatrixKrKsNaL') %Save the matrix

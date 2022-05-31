%     Copyright (C) 2022 Jordi Llopis. Contact: jorllolo@etsii.upv.es
function [ time,X,IsJs] = runORdmD(Kr_effect, Ks_effect, NaL_effect, BeatsSaved)
% This function simulates the action potential model with various parameters
% INPUTS:
% Kr_effect: scale factor (between 0 and 1) used to modified IKr
% Ks_effect: scale factor (between 0 and 1) used to modified IKs
% NaL_effect: scale factor (between 0 and 1) used to modified IKNaL
% BeatsSaved: number of beats saved

% OUTPUTS:
% time - cell array (dimensions: 1 by BeatsSaved). Each element contains a time vector; the i-th element gives the timeline of the i-th
% action potential
%
% X - cell array (dimensions: 1 by BeatsSaved). Each element contains a matrix; the i-th element gives the matrix of state variables
% (#rows = length of time vector, columns are state variables).
%
% IsJs - cell array (dimensions: 1 by BeatsSaved). Each element contains a matrix; the i-th element gives the matrix of ionic currents
% values (#rows = length of time vector, columns are currents).

beats=500; CL=1000; % Run simulation for 501 beats with a basic cycle length of 1000 ms
load('X0.mat')
model='endo';
time = cell(BeatsSaved,1); 
X = cell(BeatsSaved,1);
IsJs= cell(BeatsSaved,1);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
options=[];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
pos=1;
for n=1:beats
    if n <= beats-BeatsSaved
        [time_null, X_null]=ode15s(@ORdmD,[0 CL],X0,options,1,Kr_effect, Ks_effect, NaL_effect,model);
        X0=X_null(end,:);
    elseif n > beats-BeatsSaved
        [time{pos,1}, X{pos,1}]=ode15s(@ORdmD,[0 CL],X0,options,1,Kr_effect, Ks_effect, NaL_effect,model);
        X0=X{pos,1}(size(X{pos,1},1),:);
        pos=pos+1;
    end
end

for b=1:BeatsSaved
    for i=1:size(X{b},1)
        IsJs{b,1}(i,:) = ORdmD(time{b}(i),X{b}(i,:),0,Kr_effect, Ks_effect, NaL_effect,model);
    end
end
end
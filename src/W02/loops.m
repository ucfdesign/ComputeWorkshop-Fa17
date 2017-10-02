%% loops.m
%
% Josh Kaplan
% jk@ucf.edu
% 
% Here is an example of a loops in Matlab/Octave
% 
close all; clear all; clc

% This is an example of a for-loop
for i=1:10
    fprintf('%d ', i)
end
fprintf('\n')

% This is an example of a while-loop
i = 1;
while i <= 10   
    fprintf('%d ', i)
    i = i + 1;          
end
fprintf('\n')

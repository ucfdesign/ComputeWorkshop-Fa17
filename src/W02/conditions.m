%% conditions.m
%
% Josh Kaplan
% jk@ucf.edu
%
% An example of if/else statements in MATLAB
%
close all; clear all; clc

x = 10;

if mod(x, 2) == 0
    fprintf('You entered an even number!\n')
elseif x < 10
    fprintf('x is less than 10!\n')
elseif x > 10 && x < 20
    fprintf('x between 10 and 20!\n')
else
    fprintf('You entered an odd number!\n')
end

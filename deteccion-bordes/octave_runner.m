%{
    This script allows running an octave program that receives command line arguments,
    useful for running multiple test unattended.
%}

%#!/usr/bin/octave -qfW
close all;
clear all;
pkg load image


arg_list = argv ();
getArg = @(number) str2double(arg_list{number});

filename = arg_list{1};
threshold = getArg(2);
canny_sobel(strcat('',filename),threshold);

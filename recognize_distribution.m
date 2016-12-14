function distribution = recognize_distribution(data,N)
%把数据data输入，给定N，实现把数据data分成N组，每组的个数存在distribution中
min_data = min(data);
max_data = max(data);
step = (max_data-min_data)/N;
len = length(data);
distribution = zeros(1,N+1);
for i = 1:len
    k = floor((data(i)-min_data)/step);
    distribution(k+1) = distribution(k+1) + 1;
end



function distribution = recognize_distribution(data,N)
%������data���룬����N��ʵ�ְ�����data�ֳ�N�飬ÿ��ĸ�������distribution��
min_data = min(data);
max_data = max(data);
step = (max_data-min_data)/N;
len = length(data);
distribution = zeros(1,N+1);
for i = 1:len
    k = floor((data(i)-min_data)/step);
    distribution(k+1) = distribution(k+1) + 1;
end



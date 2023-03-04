#include <vector>
#include <string>
#include <sstream>
#include <iostream>

std::vector<std::string> split(std::string const&input)	{
	std::vector<std::string> fs;
	std::string temp;
	std::stringstream ss(input);
	while (std::getline(ss, temp))
		fs.push_back(temp);
	return fs;

}

int longestPath(std::vector<std::string> splitted)	{
	for (std::string str : splitted)
		std::cout << str << std::endl;
	std::vector<int> depth(1, 0);
	int maxlen = 0;
	for (std::string str : splitted){
		int pos = str.find_last_of('\t') + 1;
		while ((1 + pos) < depth.size())
			depth.pop_back();
		depth.push_back(depth.back() + str.length() - (pos ? pos - 1 : pos));
		splitted.pop_back();
		if (str.find('.') != std::string::npos)
			maxlen = depth.back() > maxlen? depth.back() : maxlen;
	}
	return maxlen;
}

int main(void)	{
	int longest = longestPath(split("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"));
	std::cout << "longest path: " << longest << std::endl << std::endl;
	longest = longestPath(split("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"));
	std::cout << "longest path: " <<  longest << std::endl << std::endl;
}

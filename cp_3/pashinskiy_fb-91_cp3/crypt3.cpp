

#include <iostream>
#include <string>
#include <windows.h>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>

std::string alph = "абвгдежзийклмнопрстуфхцчшщьыэюя";
int kv = pow(alph.length(), 2);
std::string textd;
struct pair {
    double n;
    std::string s;
    pair() {
        n = 0;
        s = "";
    }
    void set(double k, char a, char b) {
        n = k;
        s.push_back(a);
        s.push_back(b);
    }
    friend std::ostream& operator << (std::ostream& ostr, pair& x) {
        ostr << x.s << " " << x.n;
        return ostr;


    }
};


int mod(int a, int mod) {
    int r = a % mod;
    return r < 0 ? r + mod : r;
}

int gcd(int a, int b)
{
    a = abs(a);
    b = abs(b);
    while (a != 0 and b != 0)
    {
        if (a > b)
        {
            a = mod(a,b);
        }
        else
        {
            b =mod(b,a);
        }

    }
    return (a + b);
}


int euclidobrat(int c, int mod) 
      
    {
         if (c < 0) {
             c = mod + c;
           }
        

        int u1 = mod;
        int u2 = 0;
        int v1 = c;
        int v2 = 1;

        while (v1 != 0)
        {
            int q = u1 / v1;
            int t1 = u1 - q * v1;
            int t2 = u2 - q * v2;
            u1 = v1;
            u2 = v2;
            v1 = t1;
            v2 = t2;
        }

        return u1 == 1 ? (u2 + mod) % mod : -1;
    }

double bifreqent(std::string s, std::string alpha) {
    double bient = 0;

    for (int i = 0; i < alpha.length(); i++) {
        for (int j = 0; j < alpha.length(); j++) {
            double count = 0;
            for (int m = 0; m < s.length() - 1; m++) {
                if (alpha[i] == s[m] && alpha[j] == s[m + 1]) {


                    count++;


                }

            }
            if (count != 0) {
                bient += -0.5 * count / (s.length() - 1) * log2(count / (s.length() - 1));
            }
            


        }
    }
    return bient;
}

pair *  bicount(std::string s, std::string alpha) {
    std::vector<pair> v;
    pair * top=new pair[5];
    int z = 0;
    for (int i = 0; i < alpha.length(); i++) {
        for (int j = 0; j < alpha.length(); j++) {
            double count = 0;
            std::cout << alpha[i] << alpha[j] << " ";
            for (int m = 0; m < s.length() - 1; m+=2) {
                if (alpha[i] == s[m] && alpha[j] == s[m + 1]) {


                    count++;


                }

            }
            pair* mass = new pair();
            mass->set(count,alpha[i], alpha[j]);
            v.push_back(*mass);
           
            std::cout << count/s.length()<< std::endl;


        }
    }
    std::sort(v.begin(),v.end(),[](const pair& p1, const pair& p2) -> bool
        {
            return p1.n > p2.n;
        }
    );
    
    for (auto i = v.begin(); i != v.end(); ++i) {
       std::cout << *i << std::endl;
    }
    auto i = v.begin();
    for (int j = 0; j<5; j++) {
        top[j] = *i;
        ++i;
    }
    return top;
}

std::string decode(std::string text, int a, int b, std::string alpha) {
    std::string rez="";
    for (int i = 0; i < text.length() - 1; i+=2) {
        int aobr = euclidobrat(a, kv);
        int fen = alpha.find_first_of(text[i]);
        int sen = alpha.find_first_of(text[i + 1]);
        int y = (fen * alpha.length() +sen );
        int x = mod(aobr * (y-b),kv);
        int x2 = mod(x, alpha.length());
        int x1 =( (x-x2)/alpha.length());
        rez.push_back(alpha[x1]);
        rez.push_back(alpha[x2]);

    }
    return rez;
}

void excluse(std::string text,int x1, int x2, int y1, int y2) {
   
    int d = gcd((x1 - x2), kv);
    if ((y1 - y2) % d == 0) {
        int a0 = (x1 - x2) / d;
        int b0 = (y1 - y2) / d;
        int mod0 = kv / d;

        int x0 = mod(b0 * euclidobrat(a0, mod0), mod0);
        std::cout << "x0" << x0 << std::endl;
        for (int i = 0; i < d; i++) {
            int a = x0 + i * mod0;
            int b = mod((y1 -a * x1), kv);
         
            if (bifreqent(decode(textd, a, b, alph), alph) > 4.0 && bifreqent(decode(textd, a, b, alph), alph) < 4.15) {
               
                std::cout << "a:" << a << " b:" << b << std::endl;
                std::cout << decode(textd, a, b, alph);
                std::cout << std::endl;
            }

        }
    }
}


void ab(int&a,int&b,pair k,pair n,std::string pop1, std::string pop2, std::string alpha) {
        
        int y1 = alpha.find_first_of(k.s[0]) * alpha.length() + alpha.find_first_of(k.s[1]);
        int y2 = alpha.find_first_of(n.s[0]) * alpha.length() + alpha.find_first_of(n.s[1]);
        int x1= alpha.find_first_of(pop1[0]) * alpha.length() + alpha.find_first_of(pop1[1]);
        int x2 = alpha.find_first_of(pop2[0]) * alpha.length() + alpha.find_first_of(pop2[1]);
        if (gcd((x1 - x2), kv)==1 ) {
            a = mod(( euclidobrat((x1 - x2), kv)* (y1 - y2)), kv);
            b =mod( (y1 - a * x1), kv);
        
        }
        else if (gcd((x1 - x2), kv) > 1) {
            excluse(textd,x1, x2, y1, y2);

        }
       
      
;
}



int main()
{
    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
   
    std::string s;
    std::ifstream in("15.txt");
    if (in.is_open()) {
        while (getline(in, s)) {
            textd += s;
        }
        in.close();
    }
    pair* top=bicount(textd, alph);
    std::string pop[5] = { "ст","но","то","на","ен" };
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            for (int k = 0; k < 5; k++) {
                for (int m = 0; m < 5; m++) {
                    if (top[i].s != top[j].s && pop[k] != pop[m]) {
                        int a, b;
                        ab(a,b,top[i], top[j], pop[k], pop[m], alph);
                        if (bifreqent(decode(textd, a, b, alph),alph)>4.0 && bifreqent(decode(textd, a, b, alph), alph)<4.15) {
                            
                            std::cout << "a:" << a << " b:" << b << std::endl;
                            std::cout << decode(textd, a, b, alph);
                            std::cout << std::endl;
                            return 0;
                        }

                    }
                }
            }
        }
    }
    return 0;
}


#include <iostream>
#include <cctype>
#include <fstream>
#include <string>
#include <cmath>
#define Rus "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЮЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя"
#define RusP " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЮЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя"
using namespace std;

float logtwo(float a)
{
    return log(a) / log(2);
}

struct Node {
    string data;
    int count=0;
    Node* next, * prev;
};

class Queue
{
    Node* Head, * Tail;
public:
    int elements = 0;
    int alphabet = 0;
    Queue() :Head(NULL), Tail(NULL) {};
    ~Queue();
    void ADD(char letter);
    void biAdd(string bigr);
    bool find(char letter);
    bool bifind(string bigr);
    void Show();
    void MatrixShow(string alph);
    float Entropy();
    float findKey(string key);
};

Queue::~Queue()
{
    Node* temp;
    while (Head)
    {
        temp = Head->next;
        delete Head;
        Head = temp;
    }
}

float Queue::Entropy()
{
    float n=0;
    Node* temp = Head;
    float b = 0;
    while (temp != NULL)
    {
        float a = 0;
        a = (float)temp->count / elements;
        b = a * logtwo(a);
        n -= b;
        temp = temp->next;
    }
    return n;
}
void Queue::Show()
{
    Node* temp = Head;
    ofstream fout;
    fout.open("E:\\вывод.txt", ios_base::app);
    while (temp != NULL)
    {
        float a = 0;
        a =  (float)temp->count / elements;
      // a = floor(a * 10000)/10000;
        cout << temp->data<< "\t"<<temp->count<<"\t" << a << endl;
       // fout << temp->data << "\t" << a << endl;
        temp = temp->next;
    }
   // fout << "------------------------------------\n";
    fout.close();
}
float Queue::findKey(string key)
{
    Node* temp = Head;
    while (temp != NULL)
    {
        if (temp->data == key)
        {
            float a = 0;
            a = (float)temp->count / elements;
            return a;
        }
        temp = temp->next;
    }
    return 0;
}


void Queue::MatrixShow(string alph)
{
    string alpha = alph;
    ofstream fout;
    fout.open("E:\\вывод.txt", ios_base::app);
    for (int i = 0; i < alpha.size(); i++)
    {
        string a = { 0 };
        a= alpha[i];
        for (int y = 0; y < alpha.size(); y++)
        {
            string b;
            b = alpha[y];
            a += b;
            //cout << a << "\t";
            cout << findKey(a) << "\t";
            fout << findKey(a) << "\t";
            a = alpha[i];
          
        }
        cout << endl;
        fout << endl;
    }
    fout.close();

}

bool Queue::find(char letter)
{
    Node* temp = Head;
    while (temp != NULL)
    {
        if (temp->data[0] == letter)
        {
            temp->count++;
            elements++;
            return true;
        }
        temp = temp->next;
    }
    return false;

}
void Queue::ADD(char letter)
{
    if (find(letter))
    {
        return;
    }
    else
    {
        Node* temp = new Node;
        temp->next = NULL;
        temp->data = letter;
        temp->count++;
        if (Head != NULL)
        {
            temp->prev = Tail;
            Tail->next = temp;
            Tail = temp;
        }
        else
        {
            temp->prev = NULL;
            Head = Tail = temp;
        }
        elements++;
        alphabet++;
    }
}
bool Queue::bifind(string bigr)
{
    Node* temp = Head;
    while (temp != NULL)
    {
        if (temp->data == bigr)
        {
            temp->count++;
            elements++;
            return true;
        }
        temp = temp->next;
    }
    return false;
}
void Queue::biAdd(string bigr)
{
    if (bifind(bigr))
    {
        return;
    }
    else
    {
        Node* temp = new Node;
        temp->next = NULL;
        temp->data = bigr;
        temp->count++;
        if (Head != NULL)
        {
            temp->prev = Tail;
            Tail->next = temp;
            Tail = temp;
        }
        else
        {
            temp->prev = NULL;
            Head = Tail = temp;
        }
        elements++;
        alphabet++;
    }
}

void Task1()
{
    Queue TaskOne;
    ifstream read("E:\\text2.txt");
    string line;
    if (read.is_open())
    {
        cout << "File Read Successfully \n";
        while (getline(read, line))
        {
            string b;
            int i = 0;
            while (line[i])
            {
                if (strchr(Rus, line[i]))
                {
                    if (toupper(line[i]))
                    {
                        line[i] = tolower(line[i]);
                    }
                    b += line[i];
                }
                i++;
            }
            i = 0;
            while (b[i])
            {
                    TaskOne.ADD(b[i]);
                i++;
            }

        }
    }
    else
    {
        cout << "File Read ERROR!\n";
    }
    read.close();
    //TaskOne.Show();
    cout << "Entropy 1: " << TaskOne.Entropy() << endl;
    cout << TaskOne.elements<<endl;
}
void Task11()
{
    Queue TaskOne;
    ifstream read("E:\\text2.txt");
    string line;
    if (read.is_open())
    {
        cout << "File Read Successfully \n";
        while (getline(read, line))
        {
            int i = 0;
            while (line[i])
            {
                if (strchr(RusP, line[i]))
                {
                    if (toupper(line[i]))
                    {
                        line[i] = tolower(line[i]);
                    }
                    TaskOne.ADD(line[i]);
                }
                i++;
            }
        }
    }
    else
    {
        cout << "File Read ERROR!\n";
    }
    read.close();
   // TaskOne.Show();
    cout << "Entropy 1: " << TaskOne.Entropy() << endl;
    cout << TaskOne.alphabet << endl;
}
void Task2()
{

    Queue TaskTwo;

    ifstream read("E:\\text2.txt");
    string line;
    if (read.is_open())
    {
        cout << "File Read Successfully \n";
        while (getline(read, line))
        {
            int i = 0;
            string aft;
            while (line[i])
            {
                if (strchr(Rus, line[i]))
                {
                    if (toupper(line[i]))
                    {
                        aft += tolower(line[i]);
                    }
                }
                i++;
            }
            if (aft.size() % 2 == 0)
            {
                for (int i = 0; i < aft.size(); i += 2)
                {
                    string bigr;
                    bigr += aft[i];
                    bigr += aft[i + 1];
                    TaskTwo.biAdd(bigr);
                }
            }
            else
            {
                aft.pop_back();
                for (int i = 0; i < aft.size(); i += 2)
                {
                    string bigr;
                    bigr += aft[i];
                    bigr += aft[i + 1];
                    TaskTwo.biAdd(bigr);
                }
            }
        }
    }
    else
    {
        cout << "File Read ERROR!\n";
    }
    read.close();
    string alph = "абвгдежзийклмнопрстуфхцчшщъыьэюя";
 //   TaskTwo.MatrixShow(alph);
    //TaskTwo.Show();
    cout << "Entropy 2: " << TaskTwo.Entropy() / 2 << endl;
    cout << TaskTwo.alphabet << endl;;
}
void Task2n()
{

    Queue TaskTwo;

    ifstream read("E:\\text2.txt");
    string line;
    if (read.is_open())
    {
        cout << "File Read Successfully \n";
        while (getline(read, line))
        {
            int i = 0;
            string aft;
            while (line[i])
            {
                if (strchr(RusP, line[i]))
                {
                    if (toupper(line[i]))
                    {
                        aft += tolower(line[i]);
                    }
                }
                i++;
            }
            if (aft.size() % 2 == 0)
            {
                for (int i = 0; i < aft.size(); i += 2)
                {
                    string bigr;
                    bigr += aft[i];
                    bigr += aft[i + 1];
                    TaskTwo.biAdd(bigr);
                }
            }
            else
            {
                aft.pop_back();
                for (int i = 0; i < aft.size(); i += 2)
                {
                    string bigr;
                    bigr += aft[i];
                    bigr += aft[i + 1];
                    TaskTwo.biAdd(bigr);
                }
            }
        }
    }
    else
    {
        cout << "File Read ERROR!\n";
    }
    read.close();
    string alph = " абвгдежзийклмнопрстуфхцчшщъыьэюя";
    //TaskTwo.MatrixShow(alph);
    //TaskTwo.Show();
    cout << "Entropy 2: " << TaskTwo.Entropy() / 2 << endl;
    cout << TaskTwo.alphabet << endl;;
}

void Task21()
{

    Queue TaskTwo;
    ifstream read("E:\\text2.txt");
    string line;
    if (read.is_open())
    {
        cout << "File Read Successfully \n";
        while (getline(read, line))
        {
            int i = 0;
            string aft;
            while (line[i])
            {
                if (strchr(Rus, line[i]))
                {
                    if (toupper(line[i]))
                    {
                        aft += tolower(line[i]);
                    }
                }
                i++;
            }
            for (int i = 0; i < aft.size(); i++)
            {
                string bigr;
                bigr += aft[i];
                bigr += aft[i + 1];
                TaskTwo.biAdd(bigr);
            }
            
        }
    }
    else
    {
        cout << "File Read ERROR!\n";
    }
    read.close();
    string alph = "абвгдежзийклмнопрстуфхцчшщъыьэюя";
  //  TaskTwo.Show();
   // TaskTwo.Show();
    cout << "Entropy 2: " << TaskTwo.Entropy() / 2 << endl;
    cout << TaskTwo.alphabet << endl;;
}
void Task21n()
{

    Queue TaskTwo;

    ifstream read("E:\\text2.txt");
    string line;
    if (read.is_open())
    {
        cout << "File Read Successfully \n";
        while (getline(read, line))
        {
            int i = 0;
            string aft;
            while (line[i])
            {
                if (strchr(RusP, line[i]))
                {
                    if (toupper(line[i]))
                    {
                        aft += tolower(line[i]);
                    }
                }
                i++;
            }
            for (int i = 0; i < aft.size(); i++)
            {
                string bigr;
                bigr += aft[i];
                bigr += aft[i + 1];
                TaskTwo.biAdd(bigr);
            }

        }
    }
    else
    {
        cout << "File Read ERROR!\n";
    }
    read.close();
   // TaskTwo.Show();
    string alph = " абвгдежзийклмнопрстуфхцчшщъыьэюя";
   // TaskTwo.MatrixShow(alph);
    cout << "Entropy 2: " << TaskTwo.Entropy() / 2 << endl;
    cout << TaskTwo.alphabet << endl;;
}
int main()
{
    setlocale(LC_ALL, "Russian");
    //Task1();
   // Task11();
   // Task2();
   // Task21();
      Task2n();
      Task21n();
}
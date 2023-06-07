#include "stdio.h" 
#include <stdlib.h> 
#include <conio.h> 
#define getpch(type) (type*)malloc(sizeof(type)) 
#define NULL 0 


struct pcb { /* ������̿��ƿ�PCB */
	char name[10];
	char state;	//״̬
	int super;	//����ʱ��
	int ntime;	//��Ҫʱ��
	int rtime;	//������ʱ��
	struct pcb* link;
}*ready = NULL, * p;
typedef struct pcb PCB;

float ans = 0; //��¼��תʱ��֮��
int h = 0;	//h��ʾ��ǰ����ʱ��

void input_sort()	//��������ʱ�佨����������
{
	PCB* first, * second;
	int insert = 0;
	if ((ready == NULL) || ((p->ntime) < (ready->ntime)))
	{
		p->link = ready;
		ready = p;
	}
	else /* ���̱Ƚ�����ʱ��,�����ʵ���λ����*/
	{
		first = ready;
		second = first->link;
		while (second != NULL)
		{
			if ((p->ntime) < (second->ntime)) /*��������̱ȵ�ǰ��������ʱ���,*/
			{ /*���뵽��ǰ����ǰ��*/
				p->link = second;
				first->link = p;
				second = NULL;
				insert = 1;
			}
			else /* ����������������,����뵽��β*/
			{
				first = first->link;
				second = second->link;
			}
		}
		if (insert == 0) first->link = p;
	}
}

void input() /* �������̿��ƿ麯��*/
{
	int i, num;
	//clrscr(); /*����*/
	system("cls");
	printf("\n �������������:");
	scanf_s("%d", &num);
	for (i = 0; i < num; i++)
	{
		printf("\n ���̺�No.%d:\n", i);
		p = getpch(PCB);
		printf("\n ���������:");
		scanf_s("%s", p->name, 20);
		printf("\n ������̵���ʱ��:");
		scanf_s("%d", &p->super);
		printf("\n �����������ʱ��:");
		scanf_s("%d", &p->ntime);
		printf("\n");
		p->rtime = 0; p->state = 'w';
		p->link = NULL;
		input_sort();
	}
}

int space()
{
	int l = 0; PCB* pr = ready;
	while (pr != NULL)
	{
		l++;
		pr = pr->link;
	}
	return(l);
}

void disp(PCB* pr) /*����������ʾ����,������ʾ��ǰ����*/
{
	printf("\n qname \t state \t super \t ndtime \t runtime \n");
	printf("|%s\t", pr->name);
	printf("|%c\t", pr->state);
	printf("|%d\t", pr->super);
	printf("|%d\t", pr->ntime);
	printf("|%d\t", pr->rtime);
	printf("\n");
}

void check() /* �������̲鿴���� */
{
	PCB* pr = NULL;
	printf("\n **** ��ǰ�������еĽ�����:%s", p->name); /*��ʾ��ǰ���н���*/
	disp(p);
	pr = ready;
	printf("\n ****��ǰ��������״̬Ϊ:\n"); /*��ʾ��������״̬*/
	while (pr != NULL)
	{
		if(pr->state != 'f' && pr->super <= h && pr!=p)
			disp(pr);
		pr = pr->link;
	}
}

void destroy() /*�������̳�������(�������н���,��������)*/
{
	printf("\n ���� [%s] �����,����תʱ��Ϊ:%d,���Ȩ��תʱ��Ϊ:%.3f\n", p->name, h - p->super, (h - p->super * 1.0) / p->rtime);
	ans += (h - p->super * 1.0) / p->ntime;
	p->state = 'f';
}

void running() /* �������̾�������(��������ʱ�䵽,�þ���״̬*/
{
	printf("\n The execute number:%d \n", h);
	check();
	(p->rtime)++;
	h += 1;
	if (p->rtime == p->ntime)
	{
		destroy(); /* ����destroy����*/
		system("pause");
		system("cls");
		return;
	}
	else
	{
		p->state = 'w';
	}
	printf("\n ����һ������......");
	system("pause");
	system("cls");
	if (p->rtime != p->ntime)
		running();
}


void main() /*������*/
{
	int len;
	char ch;
	input();
	len = space();
	while ((len != 0) && (ready != NULL))
	{
		ch = getchar();
		p = ready;
		while (p->super > h || p->state == 'f')
		{
			p = p->link;
			if (p == NULL)
			{
				printf("\n\n �����Ѿ����.ƽ����Ȩ��תʱ��Ϊ:%.3f\n", ans / len);
				system("pause");
				system("cls");
				return;
			}
		}
		p->state = 'R';
		running();
	}
	return;
}

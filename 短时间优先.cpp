#include "stdio.h" 
#include <stdlib.h> 
#include <conio.h> 
#define getpch(type) (type*)malloc(sizeof(type)) 
#define NULL 0 


struct pcb { /* 定义进程控制块PCB */
	char name[10];
	char state;	//状态
	int super;	//到达时间
	int ntime;	//需要时间
	int rtime;	//已运行时间
	struct pcb* link;
}*ready = NULL, * p;
typedef struct pcb PCB;

float ans = 0; //记录周转时间之和
int h = 0;	//h表示当前运行时间

void input_sort()	//根据运行时间建立就绪队列
{
	PCB* first, * second;
	int insert = 0;
	if ((ready == NULL) || ((p->ntime) < (ready->ntime)))
	{
		p->link = ready;
		ready = p;
	}
	else /* 进程比较运行时间,插入适当的位置中*/
	{
		first = ready;
		second = first->link;
		while (second != NULL)
		{
			if ((p->ntime) < (second->ntime)) /*若插入进程比当前进程运行时间大,*/
			{ /*插入到当前进程前面*/
				p->link = second;
				first->link = p;
				second = NULL;
				insert = 1;
			}
			else /* 插入进程优先数最低,则插入到队尾*/
			{
				first = first->link;
				second = second->link;
			}
		}
		if (insert == 0) first->link = p;
	}
}

void input() /* 建立进程控制块函数*/
{
	int i, num;
	//clrscr(); /*清屏*/
	system("cls");
	printf("\n 请输入进程数量:");
	scanf_s("%d", &num);
	for (i = 0; i < num; i++)
	{
		printf("\n 进程号No.%d:\n", i);
		p = getpch(PCB);
		printf("\n 输入进程名:");
		scanf_s("%s", p->name, 20);
		printf("\n 输入进程到达时间:");
		scanf_s("%d", &p->super);
		printf("\n 输入进程运行时间:");
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

void disp(PCB* pr) /*建立进程显示函数,用于显示当前进程*/
{
	printf("\n qname \t state \t super \t ndtime \t runtime \n");
	printf("|%s\t", pr->name);
	printf("|%c\t", pr->state);
	printf("|%d\t", pr->super);
	printf("|%d\t", pr->ntime);
	printf("|%d\t", pr->rtime);
	printf("\n");
}

void check() /* 建立进程查看函数 */
{
	PCB* pr = NULL;
	printf("\n **** 当前正在运行的进程是:%s", p->name); /*显示当前运行进程*/
	disp(p);
	pr = ready;
	printf("\n ****当前就绪队列状态为:\n"); /*显示就绪队列状态*/
	while (pr != NULL)
	{
		if(pr->state != 'f' && pr->super <= h && pr!=p)
			disp(pr);
		pr = pr->link;
	}
}

void destroy() /*建立进程撤消函数(进程运行结束,撤消进程)*/
{
	printf("\n 进程 [%s] 已完成,其周转时间为:%d,其带权周转时间为:%.3f\n", p->name, h - p->super, (h - p->super * 1.0) / p->rtime);
	ans += (h - p->super * 1.0) / p->ntime;
	p->state = 'f';
}

void running() /* 建立进程就绪函数(进程运行时间到,置就绪状态*/
{
	printf("\n The execute number:%d \n", h);
	check();
	(p->rtime)++;
	h += 1;
	if (p->rtime == p->ntime)
	{
		destroy(); /* 调用destroy函数*/
		system("pause");
		system("cls");
		return;
	}
	else
	{
		p->state = 'w';
	}
	printf("\n 按任一键继续......");
	system("pause");
	system("cls");
	if (p->rtime != p->ntime)
		running();
}


void main() /*主函数*/
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
				printf("\n\n 进程已经完成.平均带权周转时间为:%.3f\n", ans / len);
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

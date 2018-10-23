#include<stdio.h>
#include<stdlib.h>
#include<string.h>


char input[100];
int ytyao(){
	if(strlen(input) == 19){
		if((int)input[4]==45 && (int)input[9]==45 && (int)input[14] == 45)
		{
			int p = (strlen(input)*strlen(input)) - strlen(input);
			int d = p * 2;
			int i = d * p;
			int check = 0;
			for(int i=0; i<strlen(input); i++){
				check += (int)input[i];
			}
			if(check == (i / ((20*4)+(3+2)*(2*2))) - d){
				printf("[-] Kyaaaaaaaa~ Kamu adalah teman Dimas!\n");
				system("cat flag.txt");
			}else{
				printf("[-] Kamu bukan teman Dimas!!\n");
				return -1;
			}

		}else{
			printf("[-] Siapa kamu ngaku - ngaku teman Dimas!\n");
			return -1;
		}

	}else{
		printf("[-] Hanya teman dimas yang bisa dapat flag!\n");
		return -1;
	}
	return 0;
}


int main(int argc, char *argv[]){
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
	printf("Teman Dimas Validator\n");
	printf("[+] Jika kamu teman Dimas masukan Passwordnya : ");
	scanf("%s", input);
	ytyao();
	return 0;
}




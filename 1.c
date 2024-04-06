int strvis(undefined2 *param_1,char *param_2,uint param_3)

{
  char *pcVar1;
  char cVar2;
  undefined2 *puVar3;
  
  cVar2 = *param_2;
  puVar3 = param_1;
  if (cVar2 == '\0') {
    *(undefined *)param_1 = 0;
    return 0;
  }
  do {
    pcVar1 = param_2 + 1;
    param_2 = param_2 + 1;
    puVar3 = vis(puVar3,(int)cVar2,param_3,*pcVar1);
    cVar2 = *param_2;
  } while (cVar2 != '\0');
  *(undefined *)puVar3 = 0;
  return (int)puVar3 - (int)param_1;
}

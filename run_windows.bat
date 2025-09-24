@echo off
echo ====================================
echo  PROJETO HPC - MONTE CARLO MPI
echo ====================================
echo.

echo 1. Teste serial...
python src\main.py
echo.

echo 2. Teste com 2 processos...
mpiexec -n 2 python src\main.py
echo.

echo 3. Teste com 4 processos...
mpiexec -n 4 python src\main.py
echo.

echo Concluido! Pressione qualquer tecla...
pause

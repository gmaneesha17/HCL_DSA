{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5eed130a-81f4-4a1c-b6f1-14ca2c7f38b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12.0\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "n=144\n",
    "print(math.sqrt(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8eecc5a9-079c-49da-9722-d73cf1bc8bf6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.141592653589793\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "print(math.pi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b71909d2-3dff-47bc-b1ce-c11399d6b11a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "69\n"
     ]
    }
   ],
   "source": [
    "from random import randint\n",
    "print(randint(1,100))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "09ef7543-9e00-437b-8c23-e2345943e91d",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'calculator'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mcalculator\u001b[39;00m\n\u001b[32m      2\u001b[39m a=\u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m())\n\u001b[32m      3\u001b[39m b=\u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m())\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'calculator'"
     ]
    }
   ],
   "source": [
    "import calculator\n",
    "a=int(input())\n",
    "b=int(input())\n",
    "print(calculator.add(a,b))\n",
    "print(calculator.sub(a,b))\n",
    "print(calculator.divide(a,b))\n",
    "print(calculator.multiply(a,b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7c515a30-6236-4a50-849d-901e48551e26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DirEntry EX_OK F_OK GenericAlias Mapping MutableMapping O_APPEND O_BINARY O_CREAT O_EXCL O_NOINHERIT O_RANDOM O_RDONLY O_RDWR O_SEQUENTIAL O_SHORT_LIVED O_TEMPORARY O_TEXT O_TRUNC O_WRONLY P_DETACH P_NOWAIT P_NOWAITO P_OVERLAY P_WAIT PathLike R_OK SEEK_CUR SEEK_END SEEK_SET TMP_MAX W_OK X_OK _AddedDllDirectory _Environ __all__ __builtins__ __cached__ __doc__ __file__ __loader__ __name__ __package__ __spec__ _check_methods _execvpe _exists _exit _fspath _get_exports_list _walk_symlinks_as_files _wrap_close abc abort access add_dll_directory altsep chdir chmod close closerange cpu_count curdir defpath device_encoding devnull dup dup2 environ error execl execle execlp execlpe execv execve execvp execvpe extsep fchmod fdopen fsdecode fsencode fspath fstat fsync ftruncate get_blocking get_exec_path get_handle_inheritable get_inheritable get_terminal_size getcwd getcwdb getenv getlogin getpid getppid isatty kill lchmod linesep link listdir listdrives listmounts listvolumes lseek lstat makedirs mkdir name open pardir path pathsep pipe popen process_cpu_count putenv read readlink remove removedirs rename renames replace rmdir scandir sep set_blocking set_handle_inheritable set_inheritable spawnl spawnle spawnv spawnve st startfile stat stat_result statvfs_result strerror supports_bytes_environ supports_dir_fd supports_effective_ids supports_fd supports_follow_symlinks symlink sys system terminal_size times times_result truncate umask uname_result unlink unsetenv urandom utime waitpid waitstatus_to_exitcode walk write "
     ]
    }
   ],
   "source": [
    "import os\n",
    "functions=dir(os)\n",
    "for fn in functions:\n",
    "    print(fn,end=\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "287739a2-3440-4b46-80bc-16ef9af65582",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\anaconda3\\Lib\\os.py\n",
      "DirEntry EX_OK F_OK GenericAlias Mapping MutableMapping O_APPEND O_BINARY O_CREAT O_EXCL O_NOINHERIT O_RANDOM O_RDONLY O_RDWR O_SEQUENTIAL O_SHORT_LIVED O_TEMPORARY O_TEXT O_TRUNC O_WRONLY P_DETACH P_NOWAIT P_NOWAITO P_OVERLAY P_WAIT PathLike R_OK SEEK_CUR SEEK_END SEEK_SET TMP_MAX W_OK X_OK _AddedDllDirectory _Environ __all__ __builtins__ __cached__ __doc__ __file__ __loader__ __name__ __package__ __spec__ _check_methods _execvpe _exists _exit _fspath _get_exports_list _walk_symlinks_as_files _wrap_close abc abort access add_dll_directory altsep chdir chmod close closerange cpu_count curdir defpath device_encoding devnull dup dup2 environ error execl execle execlp execlpe execv execve execvp execvpe extsep fchmod fdopen fsdecode fsencode fspath fstat fsync ftruncate get_blocking get_exec_path get_handle_inheritable get_inheritable get_terminal_size getcwd getcwdb getenv getlogin getpid getppid isatty kill lchmod linesep link listdir listdrives listmounts listvolumes lseek lstat makedirs mkdir name open pardir path pathsep pipe popen process_cpu_count putenv read readlink remove removedirs rename renames replace rmdir scandir sep set_blocking set_handle_inheritable set_inheritable spawnl spawnle spawnv spawnve st startfile stat stat_result statvfs_result strerror supports_bytes_environ supports_dir_fd supports_effective_ids supports_fd supports_follow_symlinks symlink sys system terminal_size times times_result truncate umask uname_result unlink unsetenv urandom utime waitpid waitstatus_to_exitcode walk write "
     ]
    }
   ],
   "source": [
    "import os\n",
    "print(os.__file__)\n",
    "for i in dir(os):\n",
    "    print(i,end=\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "63f1623d-5ac5-4420-bc72-68136380ff86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Using fallback mechanism - acts like a backup solution\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    import calculator.py\n",
    "    print(\"Module not found\")\n",
    "except ModuleNotFoundError:\n",
    "    print(\"Using fallback mechanism - acts like a backup solution\")\n",
    "    def add(a,b):\n",
    "        return a+b\n",
    "    print(add(10,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2959be70-1809-4527-8934-992be94d6bb7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

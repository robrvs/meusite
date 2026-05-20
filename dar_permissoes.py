import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meusite.settings')
django.setup()

from django.contrib.auth.models import User, Group, Permission

def dar_permissoes_completas(username):
    try:
        usuario = User.objects.get(username=username)
        
        # Tornar superusuário (tudo liberado)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save()
        
        print(f"✓ {username} agora é superusuário!")
        
    except User.DoesNotExist:
        print(f"✗ Usuário {username} não encontrado!")

# Executar
if __name__ == "__main__":
    dar_permissoes_completas('rob')
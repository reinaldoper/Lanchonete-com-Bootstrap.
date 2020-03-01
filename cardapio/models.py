from django.db import models


class Pastel(models.Model):
    nome = models.CharField(max_length=20,null=True,blank=True,verbose_name='Digite seu nome')
    endereço = models.TextField(max_length=50,null=True,blank=True,verbose_name='Digite seu endereço.')
    quantidade = models.IntegerField()
    data = models.DateTimeField(null=True,blank=True,verbose_name='Data do pedido.')
    ITALIANO = 'Italiano'
    CATUPIRI = 'Catupiri'
    FRANGO = 'Frango'
    CARNE = 'Carne'
    PIZZA = 'Pizza'
    TIPO = [
        (ITALIANO, 'Italiano'),
        (CATUPIRI, 'Catupiri'),
        (FRANGO, 'Frango'),
        (CARNE, 'Carne'),
        (PIZZA, 'Pizza'),
    ]
    Tipo_Pastel = models.CharField(
        max_length=15,
        choices=TIPO,
        default=CARNE,
        verbose_name='Escolha o tipo:'
    )

    def __str__(self):
        return self.nome


class Pizza(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=True,verbose_name='Digite seu nome')
    endereço = models.TextField(max_length=50, null=True, blank=True,verbose_name='Digite seu endereço.')
    quantidade = models.IntegerField()
    data = models.DateTimeField(null=True, blank=True,verbose_name='Data do pedido.')
    CALABREZA = 'CL'
    CATUPIRI = 'CT'
    FRANGO = 'FG'
    CARNE = 'CA'
    BANANA = 'BA'
    MUZZARELLA = 'MU'
    QUATRO_QUEIJO = '4Q'
    TIPO = [
        (CALABREZA, 'Calabreza'),
        (CATUPIRI, 'Catupiri'),
        (FRANGO, 'Frango'),
        (CARNE, 'Carne'),
        (BANANA, 'Banana'),
        (MUZZARELLA,'Muzzarella'),
        (QUATRO_QUEIJO,'Quatro queijo')
    ]
    Tipo_Pizza = models.CharField(
        max_length=2,
        choices=TIPO,
        default=CARNE,
        verbose_name='Escolha o tipo:'
    )

    def __str__(self):
        return self.nome


class Suco(models.Model):
    nome = models.CharField(max_length=20,null=True,blank=True,verbose_name='Digite seu nome')
    endereço = models.TextField(max_length=50,null=True,blank=True,verbose_name='Digite seu endereço.')
    quantidade = models.IntegerField()
    data = models.DateTimeField(null=True,blank=True,verbose_name='Data do pedido.')
    LARANJA ='LJ'
    LIMAO ='LI'
    MANGA ='MA'
    MARACAJU ='MJ'
    TIPO = [
        (LARANJA, 'Laranja'),
        (LIMAO, 'Limão'),
        (MANGA, 'Manga'),
        (MARACAJU, 'Maracaju'),
    ]
    Tipo_Suco = models.CharField(
        max_length=2,
        choices=TIPO,
        default=LARANJA,
        verbose_name='Escolha o tipo:'
    )

    def __str__(self):
        return self.nome


class Refrigerante(models.Model):
    nome = models.CharField(max_length=20,null=True,blank=True,verbose_name='Digite seu nome')
    endereço = models.TextField(max_length=50,null=True,blank=True,verbose_name='Digite seu endereço.')
    quantidade = models.IntegerField()
    data = models.DateTimeField(null=True,blank=True,verbose_name='Data do pedido.')
    LARANJA ='LJ'
    LIMAO ='LI'
    MANGA ='MA'
    MARACAJU ='MJ'
    COCA_COLA = 'CO'
    TIPO = [
        (LARANJA, 'Laranja'),
        (LIMAO, 'Limão'),
        (MANGA, 'Manga'),
        (MARACAJU, 'Maracaju'),
        (COCA_COLA,'Coca-cola')
    ]
    Tipo_Refrigerante = models.CharField(
        max_length=2,
        choices=TIPO,
        default=LARANJA,
        verbose_name='Escolha o tipo:'
    )

    def __str__(self):
        return self.nome


class Fritas(models.Model):
    nome = models.CharField(max_length=20,null=True,blank=True,verbose_name='Digite seu nome')
    endereço = models.TextField(max_length=50,null=True,blank=True,verbose_name='Digite seu endereço.')
    quantidade = models.IntegerField()
    data = models.DateTimeField(null=True,blank=True,verbose_name='Data do pedido.')
    MEDIA ='ME'
    PEQUENA ='PE'
    GRANDE ='GR'
    TIPO = [
        (MEDIA, 'Média'),
        (PEQUENA, 'Pequena'),
        (GRANDE, 'Grande'),
    ]
    Tamanho = models.CharField(
        max_length=2,
        choices=TIPO,
        default=PEQUENA,
        verbose_name='Escolha o tamanho:'
    )

    def __str__(self):
        return self.nome


class Saladas(models.Model):
    nome = models.CharField(max_length=20,null=True,blank=True,verbose_name='Digite seu nome')
    endereço = models.TextField(max_length=50,null=True,blank=True,verbose_name='Digite seu endereço.')
    quantidade = models.IntegerField()
    data = models.DateTimeField(null=True,blank=True,verbose_name='Data do pedido.')
    ALFACE ='AL'
    REPOLHO ='RE'
    PEPINO ='PE'
    TIPO = [
        (ALFACE,'Alface'),
        (REPOLHO,'Repolho'),
        (PEPINO,'Pepino'),
    ]
    Tipo_salada = models.CharField(
        max_length=15,
        choices=TIPO,
        default=ALFACE,
        verbose_name='Escolha o tipo:'
    )

    def __str__(self):
        return self.nome
# Create your models here.

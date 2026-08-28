from django.db import models


class Servico(models.Model):
    name = models.CharField(max_length=50)
    descripiton = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duracao = models.PositiveIntegerField()
    image = models.ImageField(upload_to='app/image/%y/%m/%d/', blank=True,null=True)

    def __str__(self):
        return self.name
    

class Agendamento(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)    
    nome = models.CharField(max_length=155)
    telefone = models.CharField(max_length=20)

    METODO_PAGAMENTO = [
           ('pix','Pix'),
           ('dinheiro', 'Dinheiro'),
           ('cartao', 'Cartao')
    ]
    metodo_pagamento = models.CharField(max_length=20,choices=METODO_PAGAMENTO)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f'{self.servico} - {self.nome} - {self.data} {self.horario}'

    class Meta:
      constraints = [
        models.UniqueConstraint(
            fields=['data', 'horario'],
            name='unique_agendamento_data_horario'
        )
    ]
    

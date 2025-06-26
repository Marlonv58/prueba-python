import { Component, OnInit } from '@angular/core';
import { ConsultaService } from '../servicios/consulta.service';

@Component({
  selector: 'app-consulta',
  templateUrl: './consulta.component.html',
  styleUrls: ['./consulta.component.scss']
})
export class ConsultaComponent implements OnInit {

  error: string | null = null;
  clientes: string[] = [];
  clienteId = '';
  pregunta = '';
  respuesta: any = null;

  constructor(private consultaService: ConsultaService) { }

  enviarConsulta() {
    this.error = null;
    this.respuesta = null;

    this.consultaService.consultar(this.clienteId, this.pregunta).subscribe({
      next: (data) => {
        this.respuesta = data;
      },
      error: (err) => {
        if (err.status === 0) {
          this.error = 'No se pudo conectar al backend. Verifica que el servidor esté funcionando.';
        } else if (err.status === 422) {
          this.error = 'La pregunta debe tener al menos 3 caracteres.';
        } else if (err.status === 404) {
          this.error = 'El cliente no existe o no se encontró.';
        } else {
          this.error = err.error?.detail || 'Error inesperado. Intenta nuevamente.';
        }
      },
    });
  }

  ngOnInit(): void {
    this.consultaService.getClientes().subscribe({
      next: (data) => (this.clientes = data),
      error: () => (this.clientes = []),
    });
  }

}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ConsultaService {

  private apiUrl = 'http://localhost:8000/consulta/';

  constructor(private http: HttpClient) { }

  consultar(clienteId: string, pregunta: string) {
    return this.http.post(this.apiUrl, { cliente_id: clienteId, pregunta });
  }

  getClientes() {
    return this.http.get<string[]>(this.apiUrl + 'clientes');
  }
}

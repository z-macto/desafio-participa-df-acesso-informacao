// src/api/API.ts
export default class API {
  private apiUrl: string | null = null;

  constructor() {
    // Carrega o config.json assim que a classe é instanciada
    this.loadConfig();
  }

  private async loadConfig() {
    try {
      const response = await fetch("/config.json");
      const data = await response.json();
      this.apiUrl = data.API_URL;
    } catch (error) {
      console.error("Erro ao carregar config.json:", error);
      throw new Error("Configuração da API não encontrada");
    }
  }

  // Retorna a URL da API
  async getApiUrl(): Promise<string> {
    if (!this.apiUrl) {
      await this.loadConfig();
    }
    return this.apiUrl!;
  }
}

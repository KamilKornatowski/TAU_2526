
Spis metod, endpointów i statusów
Atrapa API:
1. GET  `/transactions`  Pobiera listę  transakcji 200 OK 
2. GET  `/transactions/{id}`  Pobiera szczegóły transakcji o podanym ID  200 OK / 404 
3. POST  `/transactions`  Inicjuje nową płatność 201 Created 
4. GET  `/transactions/{id}/status`  Status płatności 200 OK 
5. DELETE  `/transactions/{id}`  Anuluje transakcję 204 No Content 
6. GET  `/methods`  Pobiera dostępne metody płatności 200 OK 
7. GET  `/methods/{type}`  Pobiera limity i stan danej metody (np. BLIK)  200 OK 
8. GET  `/customers/{id}/history`  Historia operacji klienta 200 OK 
9. POST  `/refunds` Zwrot środków dla danej transakcji 201 Created 
10. GET  `/health` dostępność i wersję systemu  200 OK 

Wykorzystane Mocha/Chai, uruchamiam `npx mocha apiService.test.js`

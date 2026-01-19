const db = require('./data.json');

class ApiService {
  // 1. GET /transactions
  getTransactions() {
    return db.transactions;
  }

  // 2. GET /transactions/{id}
  getTransactionById(id) {
    return db.transactions.find(t => t.id === id);
  }

  // 3. POST /transactions
  createNewTransaction(payload) {
    if (!payload.amount || !payload.currency) return null;
    return { ...payload, id: 999, status: "PENDING" };
  }

  // 4. GET /transactions/{id}/status
  getTransactionStatus(id) {
    return db.transaction_statuses[id] || null;
  }

  // 5. DELETE /transactions/{id}
  cancelTransaction(id) {
    const transaction = this.getTransactionById(id);
    return transaction ? true : false;
  }

  // 6. GET /methods
  getPaymentMethods() {
    return db.payment_methods;
  }

  // 7. GET /methods/{type}
  getMethodByType(type) {
    return db.payment_methods.find(m => m.type === type) || null;
  }

  // 8. GET /customers/{id}/history
  getCustomerHistory(customerId) {
    return db.customer_history[customerId] || [];
  }

  // 9. POST /refunds
  createRefund(transactionId) {
    const tx = this.getTransactionById(transactionId);
    if (!tx) return null;
    return { refund_id: "REF-" + Date.now(), status: "PROCESSING" };
  }

  // 10. GET /health
  getHealth() {
    return db.health;
  }
}

module.exports = new ApiService();
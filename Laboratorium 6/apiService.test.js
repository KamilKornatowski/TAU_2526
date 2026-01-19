const { expect } = require('chai');
const api = require('./apiService');

describe('Payment Gateway API Mock Tests (Mocha Version)', () => {

  it('1. GET /transactions - should return all transactions', () => {
    const data = api.getTransactions();
    expect(data).to.be.an('array');
    expect(data.length).to.be.at.least(1);
  });

  it('2. GET /transactions/:id - should return specific transaction', () => {
    const transaction = api.getTransactionById(1);
    expect(transaction).to.be.an('object');
    expect(transaction.id).to.equal(1);
    expect(transaction.amount).to.equal(150.00);
  });

  it('3. POST /transactions - should create and return a new transaction', () => {
    const newTx = { amount: 200, currency: 'PLN' };
    const response = api.createNewTransaction(newTx);
    expect(response.id).to.equal(999);
    expect(response.status).to.equal("PENDING");
  });

  it('4. GET /transactions/:id/status - should return status object', () => {
    const status = api.getTransactionStatus(1);
    expect(status.status).to.equal('SUCCESS');
    expect(status).to.have.property('updated_at');
  });

  it('5. DELETE /transactions/:id - should return true for existing transaction', () => {
    const isCancelled = api.cancelTransaction(1);
    expect(isCancelled).to.be.true;
  });

  it('6. GET /methods - should return list of payment methods', () => {
    const methods = api.getPaymentMethods();
    expect(methods).to.be.an('array');
    const blik = methods.find(m => m.type === 'BLIK');
    expect(blik.enabled).to.be.true;
  });

  it('7. GET /methods/:type - should return specific method details', () => {
    const cardMethod = api.getMethodByType('CARD');
    expect(cardMethod.limit).to.equal(10000);
  });

  it('8. GET /customers/:id/history - should return customer transactions', () => {
    const history = api.getCustomerHistory(101);
    expect(history).to.be.an('array');
    expect(history.length).to.equal(2);
  });

  it('9. POST /refunds - should return refund object', () => {
    const refund = api.createRefund(1);
    expect(refund).to.have.property('refund_id');
    expect(refund.status).to.equal("PROCESSING");
  });

  it('10. GET /health - should return service health status', () => {
    const health = api.getHealth();
    expect(health.status).to.equal('UP');
    expect(health.version).to.be.a('string');
  });

});
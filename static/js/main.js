function validateBid(form){
  const amount = parseFloat(form.amount.value);
  const current = parseFloat(form.current_price.value);
  if(isNaN(amount) || amount <= current){
    alert('Insira um valor maior que o preço atual.');
    return false;
  }
  return true;
}
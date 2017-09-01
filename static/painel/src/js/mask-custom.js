var maskBehavior = function (val) {
 		return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
	},options = {onKeyPress: function(val, e, field, options) {
	 	field.mask(maskBehavior.apply({}, arguments), options);
	}
};
$('.data').mask('99/99/9999');
$('.cep').mask('00000-000');
$('.telefone').mask('(00) 0000-0000');
$('.celular').mask(maskBehavior, options);
$('.cpf').mask('000.000.000-00', {reverse: true});
$('.dinheiro').mask('000.000.000.000.000,00', {reverse: true});
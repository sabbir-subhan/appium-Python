/*
 * TypeNew extends TypeEdit. 
 * The key difference is that the hasChanged method returns true for all inputs; 
 * a new item has always changed, and has no old data with which to compare.
 *
 */
function TypeNew(id, page){
	this.initTypeNew(id, page);
}
TypeNew.prototype = new TypeEdit;
TypeNew.prototype.constructor = TypeNew;
TypeNew.prototype.initTypeNew = function(id, page, type){
	this.initTypeView(id, page, type);
};
TypeNew.prototype.hasChanged = function(field){
	if (!field.Input) return false; //if this is not an input field it hasnt changed
	return true; //when creating a new item, all inputs have changed.
}
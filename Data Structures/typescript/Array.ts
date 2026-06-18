interface IMyArray<T> {
    length: number;
    data: { [index: number]: any };

    get(index: number): T | undefined; 
    push(item: any): number;
    pop(): any;
    delete(index: number): T | undefined
    shiftItem(index: number): void
}


class MyArray<T> implements IMyArray<T> {

    length: number;
    data: { [index: number]: any };

    constructor(){
        this.length = 0;
        this.data = {};
    }

    get(index: number){
        return this.data[index];
    }

    push(item: any){
        this.data[this.length] = item;
        this.length++;
        return this.length;
    }

    pop(){
        const lastItem = this.data[this.length - 1];
        delete this.data[this.length - 1];
        this.length--;
        return lastItem;
    }

    delete(index: number){
        const item = this.data[index]
        this.shiftItem(index)
        return item
    }

    shiftItem(index: number): void {
        for(let i = index; i < this.length - 1; i++){
            this.data[i] = this.data[i + 1]
        }
        delete this.data[this.length - 1];
        this.length--;
    }

    reverse(str: string){
        if(str.length < 2 || typeof str !== 'string') return "error"

        const backwards: string[] = [];
        const totalItems = str.length - 1;
        for(let i = totalItems; i >=0; i--){
            backwards.push(str[i]);
        }
        return backwards.join('')
    }
}
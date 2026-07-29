class HashTable<K, V>{
    data: Array<[K, V][] | undefined>;

    constructor(size: number) {
        this.data = new Array(size)

    }

    _hash(key: K){
        const str = String(key);
        let hash = 0;
        for(let i = 0; i < str.length; i++){
            hash = (hash + str.charCodeAt(i) * (i + 1)) % this.data.length;
        }
        return hash;
    }

    set(key: K, value: V){
        const address = this._hash(key);

        if(!this.data[address]){
            this.data[address] = [];
        }
        this.data[address]!.push([key, value]);
        return this.data;
    }

    get(key: K): V | undefined{
        const address = this._hash(key);
        const bucket = this.data[address];

        if(!bucket) return undefined;

        for(const [k, v] of bucket){
            if(k === key) return v;
        }
        return undefined;
    }
    keys(){
        const array_of_keys: K[] | undefined = []

        for (let i = 0; i < this.data.length; i++) {
            const bucket = this.data[i];
            if (bucket) {
                for (const [k] of bucket) array_of_keys.push(k);
            }
        }
        return array_of_keys;
    }
}



console.log()
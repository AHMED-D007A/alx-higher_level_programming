#!/usr/bin/node
const argv = process.argv;

const args = [];
args.push(argv[2]);
args.push(argv[3]);
const str = args.join(' is ');
console.log(str);

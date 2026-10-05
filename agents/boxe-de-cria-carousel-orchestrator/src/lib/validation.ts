import Ajv2020 from "ajv/dist/2020.js";
import {readFileSync} from "node:fs";
import {resolve} from "node:path";
import {projectRoot} from "./canon.js";
const ajv=new Ajv2020({allErrors:true,strict:false});
export function validateAgainstSchema(data:unknown,schemaPath:string):void{
  const schema=JSON.parse(readFileSync(resolve(projectRoot,schemaPath),"utf8"));
  const validate=ajv.compile(schema);
  if(!validate(data)) throw new Error("Schema validation failed: "+ajv.errorsText(validate.errors,{separator:"\n"}));
}
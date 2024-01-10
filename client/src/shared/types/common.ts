export type Status = 'idle' | 'loading' | 'failed' | 'succeeded';

export interface IError {
    message: string;
}